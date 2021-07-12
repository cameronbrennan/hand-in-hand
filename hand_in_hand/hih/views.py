from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import ClientSignupForm, ProviderSignupForm, Test

# Create your views here.
def home(request):
  return render(request, 'home.html')

def yourforms(request):
  return render(request, 'yourforms.html')

def successfullogin(request):
  return render(request, 'successfullogin.html')
 
def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Error with sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


def login_view(request):
   return render(request, 'login_view.html')

####        CLIENT VIWES
def clientlogin(request):
  return render(request, 'registration/clientlogin.html') 
          
def clientprofile(request):
  return render(request, 'client/clientprofile.html')

def yourproviders(request):
  return render(request, 'client/yourproviders.html')

def clientportal(request):
  return render(request, 'client/portal.html')
 
def clientsignup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = ClientSignupForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('clientprofile')
    else:
      error_message = 'Error with sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = ClientSignupForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/clientsignup.html', context) 
 
####        PROVIDER VIEWS 

def providerlogin(request):
  return render(request, 'registration/providerlogin.html') 

def providerprofile(request):
  return render(request, 'provider/providerprofile.html')

def yourclients(request):
  return render(request, 'provider/yourclients.html')

def providerportal(request):
  return render(request, 'provider/portal.html')

def providersignup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = ProviderSignupForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('providerprofile')
    else:
      error_message = 'Error with sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = ProviderSignupForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/providersignup.html', context) 