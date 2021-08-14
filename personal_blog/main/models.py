
from config.storage_backends import ProfileMediaStorage
from django.db import models
import uuid
from django.contrib.auth import get_user_model
from django.db.models import JSONField
from django_resized import ResizedImageField

User = get_user_model()

class City(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40, blank=True)
    temperature = models.CharField(max_length=40, blank=True)
    description = models.CharField(max_length=40, blank=True)
    icon = models.CharField(max_length=40, blank=True)
    # check if url is valid with the city name

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name_plural = "cities"


# This model has multiple fields for user setting
class Setting(models.Model):

    
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)

    # profile
    profile_pic = models.FileField(storage=ProfileMediaStorage)

    # apps
    BOOL_CHOICES= ((True, "Yes"), (False, "No"))
    todos = models.BooleanField(choices=BOOL_CHOICES, default=True)
    notes = models.BooleanField(choices=BOOL_CHOICES, default=True)
    app_display_dict = JSONField(blank=True, null=True)

    # logos
    
    def __str__(self):
        return str(self.user)

    

