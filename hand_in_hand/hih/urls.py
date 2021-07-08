from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('clients/portal/', views.clientportal, name='clientportal'),
  path('providers/portal/', views.providerportal, name='providerportal'),
  path('prprofile/', views.providerprofile, name='providerprofile'),
  path('prclients/', views.yourclients, name='clients'),
  path('clprofile/', views.clientprofile, name='clientprofile'),
  path('clproviders/', views.yourproviders, name='providers'),
  path('yourforms/', views.yourforms, name='yourforms'),
]