from django import forms
from django.forms import fields, widgets
from .models import Todo, Date
from datetime import datetime, timedelta
from django.contrib.auth import get_user_model

User = get_user_model()
today = datetime.today()
tomorrow = (datetime.today() + timedelta(days=1))
date_choices = [(today.strftime("%b %d, %Y"), "Today : {}".format(today.strftime("%b %d, %A"))), (tomorrow.strftime("%b %d, %Y"), "Tomorrow : {}".format(tomorrow.strftime("%b %d, %A")))]

#time_widget = widgets.TimeInput(attrs={'class':'timepicker'})
#time_widget.format = '%I:%M %p'

class TodoUpdateForm(forms.ModelForm):
    #start_time = forms.TimeField(input_formats=['%I:%M %p'],widget=time_widget)
    #end_time = forms.TimeField(input_formats=['%I:%M %p'],widget=time_widget)
    class Meta:
        model = Todo
        fields = ('title','task')

class TodoCreateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'task')

class DateCreateForm(forms.ModelForm):
    date = forms.DateField(input_formats=["%b %d, %Y"], widget=forms.Select(choices=date_choices))
    class Meta:
        model = Date
        fields =  ('date',)
        exclude = ('id',)
            