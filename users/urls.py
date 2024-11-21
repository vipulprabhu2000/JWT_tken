
from django.contrib import admin
from django.urls import path
from .views import RegisterAPI,LoginAPI,RegisteradminAPI,Userdata

urlpatterns = [
    path('register',RegisterAPI.as_view()),
    path('registeradmin',RegisteradminAPI.as_view()),
    path('login',LoginAPI.as_view()),
    path('Userdata',Userdata.as_view()),
    
]
