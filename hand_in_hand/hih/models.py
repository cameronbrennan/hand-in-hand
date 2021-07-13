from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Django User model includes:
# - username
# - password
# - email
# - first_name
# - last_name

# Create your models here.
# User Management options:
# - Add 'Type' to the generalized 'USER' class (single user class instead of client and provider)
# - 

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=24)
    pronouns = models.CharField(max_length=50)
    phone = models.CharField(max_length=100)
    age = models.IntegerField() # switch to date field
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # location = models.IntegerField() #zipcode? can change to str later
    def __str__(self):
        return self.first_name

class Provider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=24)
    pronouns = models.CharField(max_length=50)
    phone = models.CharField(max_length=100)
    licensure = models.CharField(max_length=100)
    def __str__(self):
        return self.first_name
    

class Assignment(models.Model):
    date = models.DateField('date assigned')
    pass

class Test(models.Model):
    pass

class Test2(models.Model):
    pass