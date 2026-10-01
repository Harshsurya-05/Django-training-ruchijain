from django.urls import path
from . views import *
urlpatterns=[
    #path("", views.home, name="home"),
    path('saveuser/', saveuser, name='saveuser'),
    path('Employeelist/', Employeelist, name='Employeelist'),
    path('updateEmployee/', updateEmployee, name='updateEmployee'),
    path('deleteEmployee/', deleteEmployee, name='deleteEmployee'),
    path('Newemployeeform/',Newemployeeform,name='Newmployeeform'),
    path('updateEmployeeform/',updateEmployeeform, name='updateEmployeeform'),

]
   