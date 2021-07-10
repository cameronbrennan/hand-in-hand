from django.forms import ModelForm
from .models import Client, Provider
from django.contrib.auth.models import User

class ClientSignupForm(ModelForm):
  class Meta:
    model = Client
    fields = ['firstname', 'lastname', 'pronouns', 'email', 'phone', 'age', 'location']
    
    
class ProviderSignupForm(ModelForm):
  class Meta:
    model = Provider
    fields = ['firstname', 'lastname', 'pronouns', 'email', 'phone', 'certification', 'certnum', 'location']
    
class Test(ModelForm):
  class Meta:
    model = Client
    fields = '__all__'