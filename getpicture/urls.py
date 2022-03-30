from django.conf.urls import url,include
from django.urls import path

from getpicture import views

urlpatterns = [
    path('upload/', views.upload, name='upload'),
    path('getUpload/', views.getUpload, name='getUpload'),
]