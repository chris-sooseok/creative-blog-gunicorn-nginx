import uuid
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Topic(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    topic = models.CharField(max_length=60)

    def __str__(self):
        return str(self.topic)

    class Meta:
        ordering = ['topic']

class Note(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE,related_name="notes",)
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=200, blank=True)
    date = models.DateField(auto_now=True)
    # content media file path is set in setting to uploads
    content = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return str(self.title)
