from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'home.html')

def providerprofile(request):
  return render(request, 'provider/providerprofile.html')

def yourclients(request):
  return render(request, 'provider/yourclients.html')

def clientprofile(request):
  return render(request, 'client/clientprofile.html')

def yourproviders(request):
  return render(request, 'client/yourproviders.html')

def yourforms(request):
  return render(request, 'yourforms.html')

def clientportal(request):
  return render(request, 'client/portal.html')

def providerportal(request):
  return render(request, 'provider/portal.html')
