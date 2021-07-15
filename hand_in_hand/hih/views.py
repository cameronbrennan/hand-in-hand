from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import ClientSignupForm, ProviderSignupForm, Test
from .models import Assignment, Gad7FormResponse, Client, Provider, Photo
from datetime import date

#### AWS PHOTO STUFF HERE
import boto3
from boto3 import client
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
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


def login_view(request):
   return render(request, 'login_view.html')

####        CLIENT VIEWS
def clientlogin(request):
  return render(request, 'registration/clientlogin.html') 
          
def clientprofile(request):
  print('client profile hit')  
  gad7_form_responses = [
    {
      'gad7_response_q1': 1, 
      'gad7_response_q2': 1, 
      'gad7_response_q3': 1,
      'gad7_response_q4': 1,
      'gad7_response_q5': 1,
      'gad7_response_q6': 1,
      'gad7_response_q7': 1
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

def gad7(request):
  model = Assignment.Gad7
  return render(request, 'client/gad7.html', { 'model': model })

def uploadgad7(request, client_id):
  # UPDATE THIS TO ARRAY FIELD
  g = Gad7FormResponse(
    gad7_response_q1=request.POST.get('gad7-choice-0'), 
    gad7_response_q2=request.POST.get('gad7-choice-1'), 
    gad7_response_q3=request.POST.get('gad7-choice-2'), 
    gad7_response_q4=request.POST.get('gad7-choice-3'), 
    gad7_response_q5=request.POST.get('gad7-choice-4'),
    gad7_response_q6=request.POST.get('gad7-choice-5'), 
    gad7_response_q7=request.POST.get('gad7-choice-6'),
    gad7_completion_date=date.today(),
    # gad7_score=gad7_response_q1+gad7_response_q2+gad7_response_q3+gad7_response_q4+gad7_response_q5+gad7_response_q6+gad7_response_q7
  )
  # WHERE DO WE LINK THIS TO A SPECIFIC CLIENT? IN HERE OR IN MODELS.PY?
  # 
  # g.client_id = client_id
  g.save()
  return redirect('home')

def read_user_gad7_forms(request):
  gad7_forms = Gad7FormResponse.objects.all()
  return render(request, 'client/forms', {'gad7_forms': gad7_forms})

# def viewgad7(request):
#   Needs to be completed when we have 
#   user_gad7 = Gad7FormResponse.get(id='')
#   return render(request, 'client/viewgad7.html', {'user_gad7': user_gad7})

# def deletegad7(request):
#   pass

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


### 

def clientdetail(request, client_id):
  print('client detail hit')
  client = Client.objects.get(id=client_id)
  return render(request, 'client/clientprofile.html', {
    'client': client, 
  })

def allclients(request):
  clients = Client.objects.all()
  return render(request, 'client/show.html', {'clients': clients})
 
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