from django.forms import ModelForm
from .models import Client, Provider
from django.contrib.auth.models import User

class ClientSignupForm(ModelForm):
  class Meta:
    model = Client
    fields = ['pronouns', 'phone', 'dob']
    
class ProviderSignupForm(ModelForm):
  class Meta:
    model = Provider
    fields = ['pronouns', 'phone', 'licensure']
    
class Test(ModelForm):
  class Meta:
    model = Client
    fields = '__all__'