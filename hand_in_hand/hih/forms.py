from django.forms import ModelForm
from .models import Client, Provider

class ClientSignupForm(ModelForm):
  class Meta:
    model = Client
    fields = ['name', 'pronouns', 'email', 'dob']
    
class ProviderSignupForm(ModelForm):
  class Meta:
    model = Provider
    fields = ['name', 'pronouns', 'email', 'certification', 'about']
