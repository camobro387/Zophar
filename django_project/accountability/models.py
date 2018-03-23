from django.db import models
from ..login.models import User

# Create your models here.


class ChuchCheckIn(models.Model):
    '''
    Contains all of the church check in data.
    '''
    checkin = models.BooleanField()
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
