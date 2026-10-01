from django.shortcuts import render
from django.http import HttpResponse

def home1(request):
    h="BRANCH NAME:- Artificial Intelligence And Data Science "
    a="HOD:- Dr VAshima Khan"
    r="ADDRESS:- 3rd Flor Main Building "
    return HttpResponse(h+a+r)
def about1(request):
    a = """<p>This is very speacial branch as well as in
    this branch feculties very smart and
    intelligence and they have very best experience
    to intract students</p>"""
    return HttpResponse(a)



