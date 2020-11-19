from django.shortcuts import render


def landing(request):
    template = 'home/landing.html'
    return render(request, template)
