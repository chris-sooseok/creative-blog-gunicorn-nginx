from django.forms import ModelForm
from .models import Note, Topic
from django import forms

class NoteForm(ModelForm):
    order = forms.Select()
    class Meta:
        model = Note
        fields = ('title','summary','order','content',)

class TopicCreateForm(ModelForm):
    class Meta:
        model = Topic
        fields = ('topic',)
        exclude = ('id',)
        