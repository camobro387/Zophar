from django.contrib import admin
from .models import ChurchCheckIn, BibleReading

# Register your models here.

admin.site.register(ChurchCheckIn)
admin.site.register(BibleReading)