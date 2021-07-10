from django.db import models
import uuid
# Create your models here.


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