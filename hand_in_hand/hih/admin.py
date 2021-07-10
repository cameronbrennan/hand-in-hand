from django.contrib import admin
from .models import Client, Provider, Assignment

# Register your models here.
admin.site.register(Client)
admin.site.register(Provider)
admin.site.register(Assignment)
# admin.site.register(User)  