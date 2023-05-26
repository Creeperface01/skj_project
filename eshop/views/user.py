from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from django.contrib.auth.decorators import login_required


@login_required
def profile(request: HttpRequest):
    return render(request, 'user/profile.html')


@login_required
def orders(request: HttpRequest):
    return render(request, 'user/orders.html')
