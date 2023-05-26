from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest


def login(request: HttpRequest):
    if request.user.is_authenticated:
        redirect('default')
    return render(request, 'auth/login.html')


def register(request: HttpRequest):
    if request.user.is_authenticated:
        redirect('default')
    return render(request, 'auth/register.html')


def logout(request: HttpRequest):
    return redirect('default')
