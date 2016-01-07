from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Test")

def detail(request, arg):
    return HttpResponse("You're looking at question %s." % arg)

def results(request, arg):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % arg)