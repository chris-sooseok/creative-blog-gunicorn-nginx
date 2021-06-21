from django.db import models
import uuid
# Create your models here.


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    date = models.DateField(auto_created=False, auto_now=False, auto_now_add=False, blank=True)
    image = models.ImageField(upload_to = 'people/')
    description = models.TextField(max_length=400, blank=True)
    

    def __str__(self):
        return self.title