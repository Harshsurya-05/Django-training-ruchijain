from django.shortcuts import render
from django.http import HttpResponse


def home2(request):
    h="BRANCH NAME:- Computer Science  "
    a="HOD:- Dr Nargis Gupta"
    r="ADDRESS:- 1st Flor Main Building "
    return HttpResponse(h+a+r)
def about2(request):
    a = """<p>This is very speacial branch as well as in
    this branch feculties very smart and
    intelligence and they have very best experience
    to intract students</p>"""
    return HttpResponse(a)