from boto3 import client
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import ClientSignupForm, ProviderSignupForm, Test
from .models import Assignment, Client, Provider, Photo, Gad7FormResponse

#### AWS PHOTO STUFF HERE
import boto3
import uuid
S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'catcollector12'



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
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


def login_view(request):
  return render(request, 'login_view.html')

####        CLIENT VIEWS

def add_photo_client(request, client_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      print({client_id})
      # print(f"{key} -< 'key', {BUCKET} - 'bucket', {s3} - 's3'")
      s3.upload_fileobj(photo_file, BUCKET, key)
      url=f"{S3_BASE_URL}{BUCKET}/{key}"
      Photo.objects.create(url=url, client_id=client_id)
    except:
      print('An error has occured uploading the file to S3')
  return redirect('clientdetail', client_id=client_id)


def clientdetail(request, client_id):
  client = Client.objects.get(id=client_id)
  return render(request, 'client/clientprofile.html', {
    'client': client, 
  })

def allclients(request):
  clients = Client.objects.all()
  return render(request, 'client/show.html', {'clients': clients})

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

# Complete gad7 view function
def gad7(request):
  model = Assignment.Gad7
  return render(request, 'client/gad7.html', model)
 
####        PROVIDER VIEWS 


def add_photo_provider(request, provider_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      # print(f"{key} -< 'key', {BUCKET} - 'bucket', {s3} - 's3'")
      s3.upload_fileobj(photo_file, BUCKET, key)
      url=f"{S3_BASE_URL}{BUCKET}/{key}"
      Photo.objects.create(url=url, provider_id=provider_id)
    except:
      print('An error has occured uploading the file to S3')
  return redirect('providerdetail', provider_id=provider_id)


def providerdetail(request, provider_id):
  provider = Provider.objects.get(id=provider_id)
  return render(request, 'provider/providerprofile.html', {
    'provider': provider, 
  })

def allproviders(request):
  providers = Provider.objects.all()
  return render(request, 'provider/show.html', {'providers': providers})

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