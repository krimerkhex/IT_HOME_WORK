from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.
def main_page(request: HttpRequest) -> HttpResponse:
    return render(request, 'main_page.html')


def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'about.html')


def second_page(request: HttpRequest) -> HttpResponse:
    return render(request, 'second_page.html')


def third_page(request: HttpRequest) -> HttpResponse:
    return render(request, 'third_page.html')
