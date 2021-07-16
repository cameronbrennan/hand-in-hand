from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'), # good
  path('accounts/signup/', views.signup, name='signup'), # good
  path('select_profile/', views.select_profile, name='select_profile'), # good
  
  # --- CLIENT URLS --- #
  path('client/create/', views.ClientCreate.as_view(), name='client_create'),
  path('client/portal/', views.clientportal, name='client_portal'),
  path('clprofile/', views.clientprofile, name='client_profile'),

  # --- PROVIDER URLS --- #
  path('provider/create/', views.ProviderCreate, name='provider_create'),
  path('provider/portal/', views.providerportal, name='provider_portal'),
  path('prprofile/', views.providerprofile, name='providerprofile'),
  
  # --- GAD-7 URLS --- #
  path('assignments/gad7/', views.gad7, name='gad7'),
  path('upload/gad7data/', views.uploadgad7, name='uploadgad7'),
  # READ and DELETE CRUD paths for the Gad7 data entities
  path('', views.viewgad7, name='viewgad7'),
  path('', views.deletegad7, name='deletegad7'),

  # LOOK AT THIS FOR DISPLAYING ALL CLIENTS
  path('client/all', views.allclients, name='allclients'),
  path('client/<int:client_id>/', views.clientdetail, name='clientdetail'),
  path('client/<int:client_id>/add_photo_client/', views.add_photo_client, name='add_photo_client'),
  path('provider/all', views.allproviders, name='allproviders'),
  path('provider/<int:provider_id>/', views.providerdetail, name='providerdetail'),
  path('provider/<int:provider_id>/add_photo_provider/', views.add_photo_provider, name='add_photo_provider'),
]