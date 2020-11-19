from django.shortcuts import render


def landing(request):
    template = 'home/landing.html'
    return render(request, template)


def home(request):
    template = 'home/home.html'
    return render(request, template)


def news(request):
    template = 'home/news.html'
    return render(request, template)
