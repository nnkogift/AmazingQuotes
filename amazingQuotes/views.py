from django.shortcuts import render

# Create your views here.

#home


def home_view(request):
    return render(request, 'index.html', {})


def custom_404(request):
    return render(request, '404-page.html', {})

#products

#about

#contact

