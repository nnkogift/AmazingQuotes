from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_protect

from blog.models import Post
from . import models
# Create your views here.

#home
from amazingQuotes.forms import ContactForm, OrderForm, EventRegistrationForm


def home_view(request):
    company = models.AmazingQuotesAbout.objects.first()
    prop = models.Product.objects.filter(feature='YES')
    posts = Post.objects.filter(feature='YES')
    ceo = models.TeamMember.objects.filter(title='CEO')
    order_form = OrderForm(request.POST or None)
    prod_id = request.GET.get('product_id')
    if get_object_or_404(models.Quote, date_of_publish=now()):
        daily_quote = get_object_or_404(models.Quote, date_of_publish=now())
    else:
        daily_quote=models.Quote.objects.first()
    if order_form.is_valid():
        instance = order_form.save(commit=False)
        order_form.instance.product_id = prod_id
        instance.save()
        messages.success(request, "Order placed successfully, We will contact you for more information ")
        return HttpResponseRedirect(redirect_to='about#alert')
    context = {
        'company': company,
        'products': prop,
        'order_form': order_form,
        'posts': posts,
        'ceo': ceo,
        'daily_quote': daily_quote

    }
    return render(request, 'index.html', context=context)


def custom_404(request):
    company = models.AmazingQuotesAbout.objects.first()
    context = {
        'company': company
    }
    return render(request, '404.html', context=context)


@csrf_protect
def about_us(request):
    company = models.AmazingQuotesAbout.objects.first()
    values = company.values.all()
    team = models.TeamMember.objects.all()
    prop = models.Product.objects.all()

    order_form = OrderForm(request.POST or None)
    prod_id = request.GET.get('product_id')
    if order_form.is_valid():
        instance = order_form.save(commit=False)
        order_form.instance.product_id = prod_id
        instance.save()
        messages.success(request, "Order placed successfully, We will contact you for more information ")
        return HttpResponseRedirect(redirect_to='about#alert')


    context = {
        'company': company,
        'team': team,
        'products': prop,
        'values': values,
        'order_form': order_form
    }
    return render(request, 'about.html', context=context)


def products(request):
    company = models.AmazingQuotesAbout.objects.first()
    prop = models.Product.objects.all()

    order_form = OrderForm(request.POST or None)
    prod_id = request.GET.get('product_id')
    if order_form.is_valid():
        instance = order_form.save(commit=False)
        order_form.instance.product_id = prod_id
        instance.save()
        messages.success(request, "Order placed successfully, We will contact you for more information ")
        return HttpResponseRedirect(redirect_to='about#alert')

    context = {
        'company': company,
        'products': prop,
        'order_form': order_form
    }
    return render(request, 'products.html', context=context)


def product(request):
    company = models.AmazingQuotesAbout.objects.all()

    context = {
        'company': company
    }
    return render(request, 'podcast-single.html', context=context)


def events(request):
    company = models.AmazingQuotesAbout.objects.first()
    events = models.Event.objects.all()
    context = {
        'company': company,
        'events': events
    }
    return render(request, 'events.html', context=context)

@csrf_protect
def event(request, id):
    company = models.AmazingQuotesAbout.objects.first()
    event = get_object_or_404(models.Event, id=id)
    form = EventRegistrationForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "You have successfully registered")
        return HttpResponseRedirect(redirect_to='event/<id>')

    context = {
        'company': company,
        'event': event,
        'form': form

    }
    return render(request, 'event-single.html', context=context)

@csrf_protect
def contact(request):
    company = models.AmazingQuotesAbout.objects.first()
    form = ContactForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Message Sent Successfully! ")
        return HttpResponseRedirect(redirect_to='contact-us')

    context = {
        'form': form,
        'company': company
    }
    return render(request, 'contact-us.html', context=context)


def coaching_list(request):
    company = models.AmazingQuotesAbout.objects.first()
    team = models.TeamMember.objects.filter(speaker='YES')
    training_list = models.TrainingTopic.objects.all()
    context = {
        'company': company,
        'team': team,
        'training_list': training_list
    }
    return render(request, 'coaching-list.html', context=context)


def coaching(request, id):
    company = models.AmazingQuotesAbout.objects.first()
    training = get_object_or_404(models.TrainingTopic, id=id)

    context = {
        'company': company,
        'training': training
    }
    return render(request, 'coaching-single.html', context=context)

