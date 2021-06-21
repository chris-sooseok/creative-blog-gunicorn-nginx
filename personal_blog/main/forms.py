from .models import City
from django import forms


unit_choceis = (("metric","Celsius"),("imperial", "Fahrenheit"))

class WeatherCreateForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ('name',)
        exclude = ('id',)
