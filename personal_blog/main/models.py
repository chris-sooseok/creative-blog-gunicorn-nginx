from django.db import models
import uuid
from django.contrib.auth import get_user_model
from django.db.models import JSONField
from django_resized import ResizedImageField
import json
from config.settings import DISPLAY_APPS
from django.core.management import call_command

User = get_user_model()

class City(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
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
    profile_pic = ResizedImageField(upload_to='profile_pic/', size=[128,128], quality=90, blank=True, null=True)

    # apps
    app_display_dict = JSONField(blank=True, null=True)

    # logos

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        if not self.app_display_dict:
            self.app_display_dict = json.dumps({APP:True for APP in DISPLAY_APPS})
        else:
            app_display_dict = json.loads(self.app_display_dict)
            keys = list(app_display_dict)
            if len(keys) < len(DISPLAY_APPS):
                for app in DISPLAY_APPS:
                    if app not in keys:
                        app_display_dict.update({app:True})
                # ['notes','todos'] != ["main","notes", "todos", "books"]
                # need to keep the state of false or ture of each app
                self.app_display_dict = json.dumps(app_display_dict)
            elif len(keys) > len(DISPLAY_APPS):
                for key in keys:
                    if key not in DISPLAY_APPS:
                        del app_display_dict[key]
                self.app_display_dict = json.dumps(app_display_dict)  
            else:
                pass
        super(Setting, self).save(*args, **kwargs)      

        
        
# user create -> setting create -> user and app_display_dict set -> now user can update setting 
# when DISPLAY_APPS updated -> gotta run migrate 

BOOL_CHOICES= ((True, "Yes"), (False, "No"))

for APP in DISPLAY_APPS:
    Setting.add_to_class(APP, models.BooleanField(choices=BOOL_CHOICES, default=True))


