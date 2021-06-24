from django.forms import ModelForm
from .models import Chapter, Book


class ChapterForm(ModelForm):
    class Meta:
        model = Chapter
        fields = ('chapter','title','content',)

class BookCreateForm(ModelForm):
    class Meta:
        model = Book
        fields = ('title',)
        exclude = ('id',)