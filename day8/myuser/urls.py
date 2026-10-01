from django.urls import path
from .views import *
urlpatterns = [
    path("signup/",signup,name='signup'),
     path("login/",login,name='login'),
      path("saveuser/",saveuser,name='saveuser'),
       path("home/",home,name='home'),
        path("loginvalidation/",loginvalidation,name='loginvalidation'),
        path("logout/",logout,name="logout"),


]