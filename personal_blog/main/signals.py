from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from .models import App

User = get_user_model()
@receiver(post_save, sender=User)
def AppCreateFunction(sender, instance, created, **kwargs):
    if created:
        App.objects.create(user=instance)

@receiver(post_save, sender=User)
def AppUpdateFunction(sender, instance, created, **kwargs):
    if created == False:
        instance.app.save()
        