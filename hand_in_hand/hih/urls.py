from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('yourforms/', views.yourforms, name='yourforms'),
  path('successfullogin/', views.successfullogin, name='successfullogin'),
  path('accounts/signup/', views.signup, name='signup'),
  path('accounts/login/', views.login, name='login'),
  path('login',views.login_view, name = 'login '),
  
  #### CLIENT URLS
  path('clients/portal/', views.clientportal, name='clientportal'),
  path('clprofile/', views.clientprofile, name='clientprofile'),
  path('clproviders/', views.yourproviders, name='providers'),
  path('accounts/clientsignup/', views.clientsignup, name='clientsignup'),
  path('registration/clientlogin/', views.clientlogin, name='clientlogin'),
  
  ##### PROVIDER URLS
  path('providers/portal/', views.providerportal, name='providerportal'),
  path('prclients/', views.yourclients, name='clients'),
  path('prprofile/', views.providerprofile, name='providerprofile'),
  path('accounts/providersignup/', views.providersignup, name='providersignup'),
  path('registration/providerlogin/', views.providerlogin, name='providerlogin'),

]