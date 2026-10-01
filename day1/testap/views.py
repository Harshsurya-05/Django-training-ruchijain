from django.shortcuts import render
from django.http import HttpResponse

def harsh(request):
    s="<h1>harsh<h1/>"
    return HttpResponse(s)
def dept(request):
    s = """
    <p>
    Department:- CSE-AIDS 5th SEM<br>
    HOD:- DR VASHIMA KHAN<br>
    ADDRESS:- 3rd FLOOR MAIN BUILDING
    </p>
    """
    return HttpResponse(s)