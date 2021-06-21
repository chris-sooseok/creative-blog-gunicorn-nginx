from django.forms import ModelForm
from .models import Note, Topic


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ('title','summary','content',)

class TopicCreateForm(ModelForm):
    class Meta:
        model = Topic
        fields = ('topic',)
        exclude = ('id',)