from django.contrib import admin
from .models import Book, Chapter
# Register your models here.


class ChapterInLine(admin.TabularInline):
    model = Chapter

class BookAdmin(admin.ModelAdmin):
    inlines = [
        ChapterInLine,
    ]
admin.site.register(Book, BookAdmin)