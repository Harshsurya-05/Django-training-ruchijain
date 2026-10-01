from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from db.models import Employee
from django.urls import reverse
# Create your views here.

def Newemployeeform(request):
    res= render(request,'Newemployeeform.html')
    return res
def saveuser(request): 
           # craete record ( c for crud)
    Eno = request.POST['Eno']
    Ename = request.POST['Ename']
    Esalary =request.POST['Esalary']
    emp = Employee(id=id,Eno=Eno,Ename=Ename,Esalary=Esalary)
    emp.save()
    url=reverse('Employeelist')
    return HttpResponseRedirect(url)

def Employeelist(request): # read data records
    Employees= Employee.objects.all()  # it returns querry set of employee object
    res = render(request,'Emplist.html',{'Employees':Employees})
    return res 
def updateEmployeeform(request):
    id=request.GET['id']
    employee=Employee.objects.filter(id=id).values()
    res=render(request,'updateEmployeeform.html',{'employee':employee[0]})
    return res

def updateEmployee(request):
    id = request.POST['id']
    Eno = request.POST['Eno']
    Ename = request.POST['Ename']
    Esalary = request.POST['Esalary']
    Employee(id=id,Eno=Eno, Ename=Ename,Esalary=Esalary).save()
    url=reverse('Employeelist')
    return HttpResponseRedirect(url)
    
def deleteEmployee(request):
    id=request.GET['id']
    emp=Employee.objects.filter(id=id)
    emp.delete()
    url=reverse('Employeelist')
    return HttpResponseRedirect(url)
def home(request):
    Employees = Employee.objects.all()
    return render(request, "Emplist.html", {"Employees": Employees})