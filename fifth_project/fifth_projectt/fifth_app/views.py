from django.shortcuts import render

from django.http import HttpResponse

def contact(request):
    return HttpResponse("This is my contact page")

def about(request):
    return HttpResponse("This is my about page")