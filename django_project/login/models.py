from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
<<<<<<< HEAD
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

=======

    # Accountability fields.
    reading_goal = models.IntegerField(null=True, blank=True)
    accountability_partner_reading = models.EmailField(null=True, blank=True)
    accountability_partner_church = models.EmailField(null=True, blank=True)

>>>>>>> 7d6c700840ef581e49d53290826217dacc9ec00c
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()