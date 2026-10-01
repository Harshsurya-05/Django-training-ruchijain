from django.urls import path
from testapp2 import views

urlpatterns=[
    path("facebook/",views.facebook),
    path("linkedin/",views.linkedin),
]