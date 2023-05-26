from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def address(request: HttpRequest):
    return render(request, 'cart/address.html')


def checkout(request: HttpRequest):
    return render(request, 'cart/checkout.html')


def complete(request: HttpRequest):
    return render(request, 'cart/complete.html')


def payment(request: HttpRequest):
    return render(request, 'cart/payment.html')


def shipping(request: HttpRequest):
    return render(request, 'cart/shipping.html')


def summary(request: HttpRequest):
    return render(request, 'cart/summary.html')

