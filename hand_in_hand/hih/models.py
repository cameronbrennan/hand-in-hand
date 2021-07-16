from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,)
    name = models.CharField(max_length=200, null=True,)
    pronouns = models.CharField(max_length=200, null=True,)
    email = models.CharField(max_length=200, null=True,)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    
class Provider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,)
    name = models.CharField(max_length=200, null=True,)
    pronouns = models.CharField(max_length=200, null=True,)
    email = models.CharField(max_length=200, null=True,)
    certification = models.CharField(max_length=150)
    about = models.TextField(max_length=500)
    
    def __str__(self):
        return self.name
    
class Assignment(models.Model):
    date = models.DateField('date assigned')

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

class Gad7FormResponse(models.Model):
    gad7_response_q1 = models.IntegerField()
    gad7_response_q2 = models.IntegerField()
    gad7_response_q3 = models.IntegerField()
    gad7_response_q4 = models.IntegerField()
    gad7_response_q5 = models.IntegerField()
    gad7_response_q6 = models.IntegerField()
    gad7_response_q7 = models.IntegerField()

    gad7_completion_date = models.DateTimeField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    # def compute_score(self):
    #     return self.gad7_response_q1 + self.gad7_response_q2 + self.gad7_response_q3 + self.gad7_response_q4 + self.gad7_response_q5 + self.gad7_response_q6 + self.gad7_response_q7

    # gad7_score = compute_score()

class Photo(models.Model):
    url = models.CharField(max_length=200)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    # provider = models.ForeignKey(Provider, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return f"Photo @{self.url}"