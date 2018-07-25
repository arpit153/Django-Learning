# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )
from .forms import UserLoginForm

# Create your views here.
def login_view(request):
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        username = form.cleaned_data.get("password")
    return render(request, "forms/login_form.html", {"form":form, "title":title})
    # user = authenticate(username='admin', password='Drc@123')
    # import pdb; pdb.set_trace()
    # # if user is not None:
    # #     # A backend authenticated the credentials
    # # else:
    #     # No backend authenticated the credentials
    # return HttpResponse("Hello, world. You're at the polls index.")

def register_view(request):
    return render(request, "login_form.html", {})

def logout_view(request):
    return render(request, "login_form.html", {})

