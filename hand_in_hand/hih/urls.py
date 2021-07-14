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
  path('assignments/gad7/', views.gad7, name='gad7'),
  path('clients/all', views.allclients, name='allclients'),
  path('clients/<int:client_id>/', views.clientdetail, name='clientdetail'),
  path('clients/<int:client_id>/add_photo_client/', views.add_photo_client, name='add_photo_client'),
  path('upload/gad7data/', views.uploadgad7, name='uploadgad7'),
  
  ##### PROVIDER URLS
  path('providers/portal/', views.providerportal, name='providerportal'),
  path('prclients/', views.yourclients, name='clients'),
  path('prprofile/', views.providerprofile, name='providerprofile'),
  #path('accounts/providersignup/', views.providersignup, name='providersignup'),
  path('registration/providerlogin/', views.providerlogin, name='providerlogin'),
  path('providers/all', views.allproviders, name='allproviders'),
  path('providers/<int:provider_id>/', views.providerdetail, name='providerdetail'),
  path('providers/<int:provider_id>/add_photo_provider/', views.add_photo_provider, name='add_photo_provider'),
  
  # path('assignments/gad7/', views.gad7, name='gad7'),
]