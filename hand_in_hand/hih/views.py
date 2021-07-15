from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Assignment, Gad7FormResponse, Client, Provider, Photo

#### AWS PHOTO STUFF HERE
import boto3
from boto3 import client
import uuid
S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'catcollector12'

# User creation and signup -- redirects to Client/Provider creation and signup
def signup(request):
  error_message=''
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('select_profile')
    else:
      error_message = 'Error with sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

# Create your views here.
def home(request):
  return render(request, 'home.html')

def select_profile(request):
  return render(request, 'select_profile.html')

####        CLIENT VIEWS

class ClientCreate(LoginRequiredMixin, CreateView):
  model = Client
  user = User
  fields = ['name', 'pronouns', 'email', 'age']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

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
      'gad7_response_q1': 2, 
      'gad7_response_q2': 2, 
      'gad7_response_q3': 2,
      'gad7_response_q4': 2,
      'gad7_response_q5': 2,
      'gad7_response_q6': 2,
      'gad7_response_q7': 2
    },
  ]
  return render(request, 'client/clientprofile.html', { 'gad7_form_responses' : gad7_form_responses })

def clientportal(request):
  return render(request, 'client/portal.html')

# ----- GAD-7 (Sample Assessment) -----#

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
  return redirect('home')

# ----- Client AWS Integration ----- #

def add_photo_client(request, client_id):
  photo_file = request.FILES.get('photo-file', None)
  print(request.FILES.get('photo-file'))
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      # print(f"{key} -< 'key', {BUCKET} - 'bucket', {s3} - 's3'")
      s3.upload_fileobj(photo_file, BUCKET, key)
      url=f"{S3_BASE_URL}{BUCKET}/{key}"
      Photo.objects.create(url=url, client_id=client_id)
    except:
      print('An error has occured uploading the file to S3')
  return redirect('clientdetail', client_id=client_id)

def clientdetail(request, client_id):
  print('client detail hit')
  client = Client.objects.get(id=client_id)
  return render(request, 'client/clientprofile.html', {
    'client': client, 
  })

# THIS PULLS ALL THE EFFIN CLIENTS

def allclients(request):
  clients = Client.objects.all()
  return render(request, 'client/show.html', {'clients': clients})
 
####        PROVIDER VIEWS 

def providerprofile(request):
  return render(request, 'provider/providerprofile.html')

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
  print('hitting provider detail')
  return render(request, 'provider/providerprofile.html', {
    'provider': provider, 
  })

def allproviders(request):
  providers = Provider.objects.all()
  return render(request, 'provider/show.html', {'providers': providers})