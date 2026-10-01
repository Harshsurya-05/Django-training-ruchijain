from django.urls import path
from testapp1 import views

urlpatterns=[
    path("home/",views.home),
    path("about/",views.about),
] 