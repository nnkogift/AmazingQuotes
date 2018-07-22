from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from . import models
# Create your views here.

#home
from amazingQuotes.forms import ContactForm


def home_view(request):
    company = models.AmazingQuotesAbout.objects.all()
    context = {
        'company': company
    }
    return render(request, 'index.html', context=context)


def custom_404(request):
    company = models.AmazingQuotesAbout.objects.all()
    context = {
        'company': company
    }
    return render(request, '404.html', context=context)


def about_us(request):
    company = models.AmazingQuotesAbout.objects.all()
    team = models.TeamMember.objects.all()
    prop = models.Product.objects.all()

    context = {
        'company': company,
        'team': team,
        'products': prop
    }
    return render(request, 'about.html', context=context)


def coaching_list(request):
    company = models.AmazingQuotesAbout.objects.all()
    context = {
        'company': company
    }
    return render(request, 'coaching-list.html', context=context)


def products(request):
    company = models.AmazingQuotesAbout.objects.all()
    context = {
        'company': company
    }
    return render(request, 'books.html', context=context)


def product(request):
    company = models.AmazingQuotesAbout.objects.all()

    context = {
        'company': company
    }
    return render(request, 'podcast-single.html', context=context)


def events(request):
    company = models.AmazingQuotesAbout.objects.all()
    events = models.Event.objects.all()
    context = {
        'company': company,
        'events': events
    }
    return render(request, 'events.html', context=context)


def event(request, id):
    company = models.AmazingQuotesAbout.objects.all()
    event = get_object_or_404(models.Event, id=id)

    context = {
        'company': company,
        'event': event

    }
    return render(request, 'event-single.html', context=context)


def contact(request):
    company = models.AmazingQuotesAbout.objects.all()
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


def coaching(request):
    company = models.AmazingQuotesAbout.objects.all()

    context = {
        'company': company
    }
    return render(request, 'coaching-single.html', context=context)