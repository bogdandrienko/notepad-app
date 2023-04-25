from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "django_notepad/home.html", context={})


def index(request):
    return HttpResponse("Hello, Arman!")
