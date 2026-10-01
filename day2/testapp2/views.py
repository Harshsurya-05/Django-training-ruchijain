from django.shortcuts import render
from django.http import HttpResponse


def facebook(request):
    s="<h1>yeh ek facebook hai</h1>"
    return HttpResponse(s)
def linkedin(request):
    s="<h1>yeh microsoft ka product hai</h1>"
    return HttpResponse(s)
