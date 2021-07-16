# --- App Imports --- #
from botocore.hooks import _FIRST
from .forms import UserSignup
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Assignment, Gad7FormResponse, Client, Provider, Photo
from datetime import date

# --- AWS3 Photo Imports --- #
import boto3
from boto3 import client
import uuid
S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'catcollector12'

# --- Create User (Redirect to Select Profile) --- #
def signup(request):
  error_message=''
  if request.method == "POST":
    form = UserSignup(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('select_profile')
    else:
      error_message = 'Error with sign up - try again'
      print(error_message)
  form = UserSignup()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

# --- Base Views --- #
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def select_profile(request):
  return render(request, 'select_profile.html')

# --- Client Specific Views --- #
class ClientCreate(LoginRequiredMixin, CreateView):
  model = Client
  fields = ['pronouns', 'age']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

@login_required
def client_portal(request):
  return render(request, 'client/portal.html')

@login_required
def client_detail(request, client_id):
  client = Client.objects.get(id=client_id)
  gad7s = client.Gad7FormResponse.get()
  print(gad7s)
  return render(request, 'client/client_detail.html', {'client': client})

def clientprofile(request, client_id):
  client = Client.objects.get(id=client_id)
  print(client)
  return render(request, 'client/clientprofile.html', { 'gad7_form_responses' : gad7_form_responses })

# ----- GAD-7 (Sample Assessment) -----#

# Complete gad7 view function
@login_required
def gad7(request):
  model = Assignment.Gad7
  return render(request, 'client/gad7.html', { 'model': model})

@login_required
def uploadgad7(request, client_id):
  print(client_id)
  client = Client.objects.get(id=client_id)
  g = Gad7FormResponse(
    gad7_response_q1=request.POST.get('gad7-choice-0'), 
    gad7_response_q2=request.POST.get('gad7-choice-1'), 
    gad7_response_q3=request.POST.get('gad7-choice-2'), 
    gad7_response_q4=request.POST.get('gad7-choice-3'), 
    gad7_response_q5=request.POST.get('gad7-choice-4'),
    gad7_response_q6=request.POST.get('gad7-choice-5'), 
    gad7_response_q7=request.POST.get('gad7-choice-6'),
    gad7_completion_date=date.today(),
  )
  g.client = client
  print(g.client)
  g.save()
  return redirect('home')

# READ and DELETE CRUD operations for the Gad7 data entity ------------------

def viewgad7(request):
  pass

def deletegad7(request):
  pass

# ----- Client AWS Integration ----- #

def allclients(request):
  clients = Client.objects.all()
  return render(request, 'client/show.html', {'clients': clients})

# - Client AWS Integration - #

@login_required
def add_photo_client(request, client_id):
  photo_file = request.FILES.get('photo-file', None)
  print(request.FILES.get('photo-file'))
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url=f"{S3_BASE_URL}{BUCKET}/{key}"
      Photo.objects.create(url=url, client_id=client_id)
    except:
      print('An error has occured uploading the file to S3')
  return redirect('client_detail', client_id=client_id)

# --- Provider Specific Views --- #
class ProviderCreate(LoginRequiredMixin, CreateView):
  model = Provider
  fields = ['pronouns', 'certification', 'about']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

@login_required    
def provider_portal(request):
  return render(request, 'provider/portal.html')

@login_required    
def provider_detail(request, provider_id):
  provider = Provider.objects.get(id=provider_id)
  return render(request, 'provider/provider_detail.html', { 'provider': provider })

def allproviders(request):
  providers = Provider.objects.all()
  return render(request, 'provider/show.html', {'providers': providers})

# - Provider AWS Integration - #

@login_required    
def add_photo_provider(request, provider_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url=f"{S3_BASE_URL}{BUCKET}/{key}"
      Photo.objects.create(url=url, provider_id=provider_id)
    except:
      print('An error has occured uploading the file to S3')
  return redirect('providerdetail', provider_id=provider_id)
