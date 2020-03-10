from django.db import models
from django.contrib.auth.models import AbstractUser

from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    email = models.EmailField()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=10)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
