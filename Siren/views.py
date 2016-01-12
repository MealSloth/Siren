from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    response = render(request, 'home.html')
    return HttpResponse(response)


def about(request):
    response = render(request, 'about.html')
    return HttpResponse(response)


def blog(request):
    response = render(request, 'blog.html')
    return HttpResponse(response)


def contact(request):
    response = render(request, 'blog.html')
    return HttpResponse(response)


def consumer(request):
    response = render(request, 'consumer.html')
    return HttpResponse(response)


def producer(request):
    response = render(request, 'producer.html')
    return HttpResponse(response)


def detail(request, arg):
    return HttpResponse("You're looking at question %s." % arg)


def results(request, arg):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % arg)