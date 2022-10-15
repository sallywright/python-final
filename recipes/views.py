from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def home_view(request):
    context = {"user_authenticated": False}
    if request.user.is_authenticated:
        context = {**context, "user_authenticated": True}
    return render(request, "home/index.html", context)


def login_view(request):
    context = {}
    return render(request, "login/index.html", context)


def register_view(request):
    context = {}
    return render(request, "register/index.html", context)
