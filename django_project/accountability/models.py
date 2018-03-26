from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ChurchCheckIn(models.Model):
    '''
    Contains all of the church check in data.
    '''
    check_in = models.BooleanField()
    # location = models.
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user) + ' ' + str(self.check_in)


class BibleReading(models.Model):
    time_read = models.IntegerField()       # in minutes
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user) + " " + str(self.time_read) + " hours"
