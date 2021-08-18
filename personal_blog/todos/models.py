import uuid
from django.core.paginator import Paginator
from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Date(models.Model):
    id = models.UUIDField(primary_key=True, db_index=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True)

    def __str__(self):
        return str(self.date)

    class Meta:
        ordering = ['-date']
      
       
class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    date = models.ForeignKey(Date, on_delete=models.CASCADE, related_name='todos',)
    start_time = models.TimeField(default=datetime.today, auto_now=False, auto_now_add=False, auto_created= False, blank=True)
    end_time = models.TimeField(default=datetime.today, auto_now=False, auto_now_add=False, auto_created= False, blank=True)
    task = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['start_time']