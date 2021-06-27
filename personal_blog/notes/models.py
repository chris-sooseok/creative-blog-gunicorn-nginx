import uuid
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Topic(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    topic = models.CharField(max_length=30)

    def __str__(self):
        return str(self.topic)

    class Meta:
        ordering = ['topic']

class Note(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE,related_name="notes",)
    title = models.CharField(max_length=50)
    summary = models.CharField(max_length=200, blank=True)
    date = models.DateField(auto_now=True)
    content = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return str(self.title)
