
from django.urls import path

from bglu import views

urlpatterns = [
    path('glu/', views.glu, name='glu'),
    path('getGlu/', views.getGlu, name='getGlu'),
    path('showList/', views.showList, name='showList'),
    path('deleteglu/', views.deleteglu, name='deleteglu'),
    path('updateglu/', views.updateglu, name='updateglu'),
    path('getGluupdate/', views.getGluupdate, name='getGluupdate')
]