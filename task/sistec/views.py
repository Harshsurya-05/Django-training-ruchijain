from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    h="full NAme:- Sagar Institu Science And Tchnology"
    a="Principle:- Dr Manish Bilore"
    r="ADDRESS:- Ghandhi nagar bhoapl "
    return HttpResponse(h+a+r)
def about(request):
    a = """<p>This is very speacial college as well as in
    this college feculties very smart and
    intelligence and they have very best experience
    to intract students</p>"""
    return HttpResponse(a)