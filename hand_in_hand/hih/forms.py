from django.forms import ModelForm
from .models import Client, Provider
from django.contrib.auth.models import User

class ClientSignupForm(ModelForm):
  class Meta:
    model = Client
    fields = ['first_name', 'last_name', 'email', 'password']
    
    
class ProviderSignupForm(ModelForm):
  class Meta:
    model = Provider
    fields = '__all__'
    
class Test(ModelForm):
  class Meta:
    model = Client
    fields = '__all__'