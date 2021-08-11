from .models import City, Setting
from django import forms


unit_choceis = (("metric","Celsius"),("imperial", "Fahrenheit"))

class WeatherCreateForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ('name',)
        exclude = ('id',)

class SettingUpdateForm(forms.ModelForm):
    class Meta:
        model = Setting
        fields = ('todos', 'notes',)
        exclude = ('user',)