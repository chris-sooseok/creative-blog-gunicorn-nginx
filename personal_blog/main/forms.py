from .models import City, Setting
from django import forms


unit_choceis = (("metric","Celsius"),("imperial", "Fahrenheit"))

class WeatherCreateForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ('name',)
        exclude = ('id',)


# This form has multiple fields for user setting update
class SettingUpdateForm(forms.ModelForm):
    class Meta:
        model = Setting
        fields = ('profile_pic','todos', 'notes',)
        exclude = ('user',)

