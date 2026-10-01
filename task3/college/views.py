from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    return render(request, "index.html")


def sistec(request):
    return render(request, "sistec.html")


def lnct(request):
    return render(request, "lnct.html")


def oriental(request):
    return render(request, "oriental.html")