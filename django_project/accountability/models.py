from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ChurchCheckIn(models.Model):
    '''
    Contains all of the church check in data.
    '''
    check_in = models.BooleanField()
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
