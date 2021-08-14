from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from .models import Setting

User = get_user_model()

# Create setting model for new user
@receiver(post_save, sender=User)
def SettingCreateFunction(sender, instance, created, **kwargs):
    if created:
        Setting.objects.create(user=instance)

# Update setting model for existing-user
@receiver(post_save, sender=User)
def SettingUpdateFunction(sender, instance, created, **kwargs):
    if created == False:
        instance.setting.save()
