from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    response = render(request, 'App/index.html')
    return HttpResponse(response)

def test(request):
    return HttpResponse("Test")

def detail(request, arg):
    return HttpResponse("You're looking at question %s." % arg)

def results(request, arg):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % arg)