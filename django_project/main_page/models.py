from django.db import models

# Create your models here.


class Page(models.Model):
    name = models.CharField(max_length=30)
    url = models.CharField(max_length=30)
    css_class = models.CharField(max_length=30, blank=True)
    order = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name