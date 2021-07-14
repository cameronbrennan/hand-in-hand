from boto3 import client
from django.shortcuts import render, redirect
from .models import Client, Provider, Assignment, Gad7FormResponse
from .forms import ClientSignupForm, ProviderSignupForm, Test
from .models import Assignment, Client, Provider, Photo, Gad7FormResponse

#### AWS PHOTO STUFF HERE
import boto3
import uuid
S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'


# Create your views here.


def home(request):
  return render(request, 'home.html')

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def signup(request):
  error_message = ''
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('successfullogin')
    else:
      error_message = 'Invalid signup - try again!'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
# ---- ^^^ User Creation and signup functional (no anchor)^^^ ---- #

# Create your views here.
def home(request):
  return render(request, 'home.html')

def yourforms(request):
  return render(request, 'yourforms.html')

def successfullogin(request):
  return render(request, 'successfullogin.html')

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


####        CLIENT VIEWS

def clientlogin(request):
  return render(request, 'registration/clientlogin.html') 
          
def clientprofile(request):  
  gad7_form_responses = [
    {
      'gad7_response_q1': 1, 
      'gad7_response_q2': 2, 
      'gad7_response_q3': 3,
      'gad7_response_q4': 3,
      'gad7_response_q5': 3,
      'gad7_response_q6': 3,
      'gad7_response_q7': 3
    },
    {
      'gad7_response_q1': 1, 
      'gad7_response_q2': 2, 
      'gad7_response_q3': 3,
      'gad7_response_q4': 3,
      'gad7_response_q5': 3,
      'gad7_response_q6': 3,
      'gad7_response_q7': 3
    },
    {
      'gad7_response_q1': 1, 
      'gad7_response_q2': 2, 
      'gad7_response_q3': 3,
      'gad7_response_q4': 3,
      'gad7_response_q5': 3,
      'gad7_response_q6': 3,
      'gad7_response_q7': 3
    },
  ]
  return render(request, 'client/clientprofile.html', { 'gad7_form_responses' : gad7_form_responses })

def yourproviders(request):
  return render(request, 'client/yourproviders.html')

def clientportal(request):
  return render(request, 'client/portal.html')
 
def clientsignup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'client' form object
    # that includes the data from the browser
    form = ClientSignupForm(request.POST)
    if form.is_valid():
      form.user_id = request.user_id
      form.save()
      return redirect('clientprofile')
    else:
      error_message = 'Error with sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = ClientSignupForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/clientsignup.html', context)

def gad7(request):
  model = Assignment.Gad7
  return render(request, 'client/gad7.html', { 'model': model })

def uploadgad7(request):
  # UPDATE THIS TO ARRAY FIELD
  g = Gad7FormResponse(
    gad7_response_q1=request.POST.get('gad7-choice-0'), 
    gad7_response_q2=request.POST.get('gad7-choice-1'), 
    gad7_response_q3=request.POST.get('gad7-choice-2'), 
    gad7_response_q4=request.POST.get('gad7-choice-3'), 
    gad7_response_q5=request.POST.get('gad7-choice-4'),
    gad7_response_q6=request.POST.get('gad7-choice-5'), 
    gad7_response_q7=request.POST.get('gad7-choice-6')
  )
  g.save()
  return redirect('clientprofile')
 
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

# def providersignup(request):
#   error_message = ''
#   if request.method == 'POST':
#     # This is how to create a 'user' form object
#     # that includes the data from the browser
#     form = ProviderSignupForm(request.POST)
#     if form.is_valid():
#       # This will add the user to the database
#       user = form.save()
#       # This is how we log a user in via code
#       login(request, user)
#       return redirect('providerprofile')
#     else:
#       error_message = 'Error with sign up - try again'
#   # A bad POST or a GET request, so render signup.html with an empty form
#   form = ProviderSignupForm()
#   context = {'form': form, 'error_message': error_message}
#   return render(request, 'registration/providersignup.html', context) 