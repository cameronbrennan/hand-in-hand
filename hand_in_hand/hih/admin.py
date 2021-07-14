from django.contrib import admin
from .models import Client, Gad7FormResponse, Provider, Assignment

# Register your models here.
admin.site.register(Client)
admin.site.register(Provider)
admin.site.register(Assignment)
admin.site.register(Gad7FormResponse)
# admin.site.register(User)  
