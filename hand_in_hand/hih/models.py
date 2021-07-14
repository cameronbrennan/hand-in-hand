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
    pronouns = models.CharField(max_length=50)
    phone = models.CharField(max_length=100)
    dob = models.DateField()
    # location = models.IntegerField() #zipcode? can change to str later
    def __str__(self):
        return self.name

class Provider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pronouns = models.CharField(max_length=50)
    phone = models.CharField(max_length=100)
    licensure = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Assignment(models.Model):
    date = models.DateField('date assigned')
    pass

    class Gad7:
        assignment_name = 'GAD-7'
        questions = [
            "How often have you been bothered by feeling nervous, anxious, or on edge over the past 2 weeks?",
            "How often have you been bothered by not being able to stop or control worrying over the past 2 weeks?",
            "How often have you been bothered by worrying too much about different things over the past 2 weeks?", 
            "How often have you been bothered by trouble relaxing over the past 2 weeks?",
            "How often have you been bothered by being so restless that it's hard to sit still over the past 2 weeks?",
            "How often have you been bothered by becoming easily annoyed or irritable over the past 2 weeks?",
            "How often have you been bothered by feeling afraid as if something awful might happen over the past 2 weeks?"
        ]
        # could make this an array as well and link the score to the indices
        choices = {
            'Not at all': 0,
            'Several days': 1,
            'More than half the days': 2,
            'Nearly every day': 3
        }

        def __init__(self):
            pass

        def __str__(self):
            return self.assignment_name

        # can use JS to grab the values selected from the DOM and add them together
        # get the template set up so a user can see all the questions first, then figure out method for computing

class Gad7FormResponse(models.Model):
    gad7_response_q1 = models.IntegerField()
    gad7_response_q2 = models.IntegerField()
    gad7_response_q3 = models.IntegerField()
    gad7_response_q4 = models.IntegerField()
    gad7_response_q5 = models.IntegerField()
    gad7_response_q6 = models.IntegerField()
    gad7_response_q7 = models.IntegerField()

    def compute_score(self):
        return self.gad7_q1_response + self.gad7_q2_response + self.gad7_q3_response + self.gad7_q4_response + self.gad7_q5_response + self.gad7_q6_response + self.gad7_q7_response

class Test(models.Model):
    pass

class Test2(models.Model):
    pass

class Photo(models.Model):
    url = models.CharField(max_length=200)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return f"Photo @{self.url}"