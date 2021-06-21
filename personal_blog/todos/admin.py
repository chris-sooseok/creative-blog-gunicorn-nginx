from django.contrib import admin
from .models import Date, Todo
# Register your models here.

class TodoInLine(admin.TabularInline):
    model = Todo
    
class DateAdmin(admin.ModelAdmin):
    inlines = [
        TodoInLine,
    ]


admin.site.register(Date, DateAdmin)