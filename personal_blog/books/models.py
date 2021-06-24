import uuid
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=30)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['title']

class Chapter(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE,related_name="chapters",)
    chapter = models.CharField(max_length=30, blank=True)
    title = models.CharField(max_length=200, blank=True)
    date = models.DateField(auto_now=True)
    content = RichTextUploadingField(blank=True, config_name='book')
    # to commit
    def __str__(self):
        return str(self.title)
