from django.shortcuts import render
from django.views.generic import View

# Create your views here.


def home(request):
    return render(request, "base-login.html", {})

def login(request):
    return render(request, "forms/signIn.html", {})