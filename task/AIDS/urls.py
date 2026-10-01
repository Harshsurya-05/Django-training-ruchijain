from django.urls import path
from AIDS import views

urlpatterns=[
    path("home1/",views.home1),
    path("about1/",views.about1),
]