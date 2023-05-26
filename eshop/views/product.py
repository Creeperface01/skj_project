from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def default(request: HttpRequest, category: str):
    return render(request, 'product/default.html')


def show(request: HttpRequest, slug: str):
    return render(request, 'product/show.html')
