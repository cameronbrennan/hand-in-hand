from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('yourforms/', views.yourforms, name='yourforms'),
  path('successfullogin/', views.successfullogin, name='successfullogin'),
  path('accounts/signup/', views.signup, name='signup'),
  path('accounts/login/', views.login, name='login'),
  
  #### CLIENT URLS
  path('clients/portal/', views.clientportal, name='clientportal'),
  path('clprofile/', views.clientprofile, name='clientprofile'),
  path('clproviders/', views.yourproviders, name='providers'),
  path('accounts/clientsignup/', views.clientsignup, name='clientsignup'),
  # path('accounts/login/', views.clientlogin, name='login'),
  
  ##### PROVIDER URLS
  path('providers/portal/', views.providerportal, name='providerportal'),
  path('prclients/', views.yourclients, name='clients'),
  path('prprofile/', views.providerprofile, name='providerprofile'),
  path('accounts/providersignup/', views.providersignup, name='providersignup'),
  # path('accounts/login/', views.providerlogin, name='login'),

]