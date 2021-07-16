from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'), # good
  path('accounts/signup/', views.signup, name='signup'), # good
  path('select_profile/', views.select_profile, name='select_profile'), # good
  
  # --- CLIENT URLS --- #
  path('client/create/', views.ClientCreate.as_view(), name='client_create'),
  path('client/portal/', views.client_portal, name='client_portal'),
  path('client/<int:client_id>/', views.client_detail, name='client_detail'),
  path('client/<int:client_id>/add_photo_client/', views.add_photo_client, name='add_photo_client'),

  # --- PROVIDER URLS --- #
  path('provider/create/', views.ProviderCreate.as_view(), name='provider_create'),
  path('provider/portal/', views.provider_portal, name='provider_portal'),
  path('provider/<int:provider_id>/', views.provider_detail, name='provider_detail'),
  path('provider/<int:provider_id>/add_photo_provider/', views.add_photo_provider, name='add_photo_provider'),

  # --- GAD-7 URLS --- #
  path('assignments/gad7/', views.gad7, name='gad7'),
]