from django.db import models
from login.models import User
from django.forms import ModelForm
# Import User when created...

# Create your models here

class Question(models.Model):
    question_text = models.CharField(max_length=200)




class Choice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    choice = models.IntegerField(default=0)


