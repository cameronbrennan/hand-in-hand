from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    pronouns = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=100)
    age = models.IntegerField()
    last_login = models.CharField(max_length=400)
    location = models.IntegerField() #zipcode? can change to str later
    # user = models.ForeignKey(User, on_delete=models.CASCADE) #add user type?
    def __str__(self):
        return self.name
    
class Provider(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    pronouns = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=100)
    about = models.TextField(max_length=500)
    certification = models.CharField(max_length=150)
    certnum = models.CharField(max_length=100)
    last_login = models.CharField(max_length=400)
    location = models.IntegerField() #zipcode? can change to str later
    # user = models.ForeignKey(User, on_delete=models.CASCADE) #add user type?
    def __str__(self):
        return self.name
    

class Assignment(models.Model):
    date = models.DateField('date assigned')

class Test(models.Model):
    pass

class Test2(models.Model):
    pass