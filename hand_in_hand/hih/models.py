from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    pronouns = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=100)
    age = models.IntegerField()
    location = models.IntegerField() #zipcode? can change to str later
    def __str__(self):
        return self.name
    
class Provider(models.Model):
    name = models.CharField(max_length=100)
    pronouns = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=100)
    about = models.TextField(max_length=500)
    certification = models.CharField(max_length=150)
    certnum = models.CharField(max_length=100)
    location = models.IntegerField() #zipcode? can change to str later
    def __str__(self):
        return self.name
    

class Assignment(models.Model):
    date = models.DateField('date assigned')
