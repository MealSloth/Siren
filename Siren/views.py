from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    response = render(request, 'page/home.html')
    return HttpResponse(response)


def about(request):
    response = render(request, 'page/about.html')
    return HttpResponse(response)


def blog(request):
    response = render(request, 'page/blog.html')
    return HttpResponse(response)


def contact(request):
    response = render(request, 'page/contact.html')
    return HttpResponse(response)


def consumer(request):
    response = render(request, 'page/consumer.html')
    return HttpResponse(response)


def producer(request):
    response = render(request, 'page/producer.html')
    return HttpResponse(response)