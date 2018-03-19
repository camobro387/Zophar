from django.db import models
from login.models import User
# Import User when created...

# Create your models here


class Question(models.Model):
    question_text = models.CharField(max_length=200)

    category = models.CharField(max_length=30,null=True)
    # gentleness/gentlenessneg

    type = models.CharField(max_length=1)
    # b = T/F
    # m = 1-5
    # r = 1-10
    # w = 1-7

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    choice = models.IntegerField(default=0)


