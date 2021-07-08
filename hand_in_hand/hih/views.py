from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'home.html')

def providerprofile(request):
  return render(request, 'providerprofile.html')

def yourclients(request):
  return render(request, 'yourclients.html')

def clientprofile(request):
  return render(request, 'clientprofile.html')

def yourproviders(request):
  return render(request, 'yourproviders.html')

def yourforms(request):
  return render(request, 'yourforms.html')

def clientportal(request):
  return render(request, 'client/portal.html')

def providerportal(request):
  return render(request, 'provider/portal.html')
