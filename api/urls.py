from django.conf.urls import url,include
from django.contrib import admin

from django.urls import path

from api import views

urlpatterns = [

    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logintest/', views.logintest, name='logintest'),
    path('addregister/', views.addregister, name='addregister'),
    # url(r'^message/', views.MessageView.as_view()),
]
