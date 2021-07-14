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

    class Gad7:
        assignment_name = 'GAD-7'
        questions = {
            '1': "How often have you been bothered by feeling nervous, anxious, or on edge over the past 2 weeks?",
            '2': "How often have you been bothered by not being able to stop or control worrying over the past 2 weeks?",
            '3': "How often have you been bothered by worrying too much about different things over the past 2 weeks?", 
            '4': "How often have you been bothered by trouble relaxing over the past 2 weeks?",
            '5': "How often have you been bothered by being so restless that it's hard to sit still over the past 2 weeks?",
            '6': "How often have you been bothered by becoming easily annoyed or irritable over the past 2 weeks?",
            '7': "How often have you been bothered by feeling afraid as if something awful might happen over the past 2 weeks?"
        }
        # could make this an array as well and link the score to the indices
        choices = {
            'Not at all': 0,
            'Several days': 1,
            'More than half the days': 2,
            'Nearly every day': 3
        }


        # put questions in an array with a series of strings, no need to add the question number since we can easily get that with the indices
        # [question1_text, ...]
        questions_and_choices = [
            [
                "How often have you been bothered by feeling nervous, anxious, or on edge over the past 2 weeks?",
                choices
            ], 
            [
                "How often have you been bothered by not being able to stop or control worrying over the past 2 weeks?", 
                choices
            ], 
            [
                "How often have you been bothered by worrying too much about different things over the past 2 weeks?",
                choices
            ],
            [
                "How often have you been bothered by trouble relaxing over the past 2 weeks?",
                choices
            ],
            [
                "How often have you been bothered by being so restless that it's hard to sit still over the past 2 weeks?",
                choices
            ],
            [
                "How often have you been bothered by becoming easily annoyed or irritable over the past 2 weeks?",
                choices
            ],
            [
                "How often have you been bothered by feeling afraid as if something awful might happen over the past 2 weeks?",
                choices
            ],
         ]
        def __init__(self):
            pass

        def __str__(self):
            return self.assignment_name

        # can use JS to grab the values selected from the DOM and add them together
        # get the template set up so a user can see all the questions first, then figure out method for computing
        def compute_score(self):
            pass
        
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