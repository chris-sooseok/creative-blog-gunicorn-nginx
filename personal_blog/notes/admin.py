from django.contrib import admin
from .models import Topic, Note
# Register your models here.


class NoteInLine(admin.TabularInline):
    model = Note

class TopicAdmin(admin.ModelAdmin):
    inlines = [
        NoteInLine,
    ]
admin.site.register(Topic, TopicAdmin)