from django.core.checks import messages
from django.shortcuts import get_object_or_404, render, redirect
import requests
from .models import City, Setting
from django.contrib.auth.decorators import login_required
from .forms import SettingUpdateForm
import json
# Create your views here.

def MainListFunction(request):
    # list of recent posts
    # list of weather
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units={}&appid=96748c1eb3fe471926e26a21bafd6c4e"
  
    cities = City.objects.all()

    message = ""
    if cities:
        for city in cities:
            r = requests.get(url.format(city.name, "metric")).json()
        # ckeditor content
            if "message" in r and (r["message"] == "city not found" or r["message"] == "Nothing to geocode"):
                City.objects.get(id=city.id).delete()
                message = "City Name is invalid"
            else:
                city = City.objects.get(id=city.id)
                city.temperature = r['main']['temp']
                city.description = r['weather'][0]['description']
                city.icon =  r['weather'][0]['icon']
                city.save()
    cities = City.objects.all()
    context = {"cities": cities, "message": message}
    
    return render(request, '_home.html', context)

def WeatherCreateFunction(request):
    if request.user.is_authenticated:
        city_name_list = request.POST['city'].split(" ")
        city_name_list = [word for word in city_name_list if word != ""]
        city_name = " ".join(map(str,city_name_list))
        City(name=city_name.title()).save()

        return redirect('home')
    else:
        return redirect('account_login')

def WeatherDeleteFunction(request, pk):
    if request.user.is_authenticated:
        city_name = City.objects.get(id=pk)
        city_name.delete()
        return redirect('home')
    else:
        return redirect('account_login')

@login_required
def SettingUpdateFunction(request):
    context = {}
    user = request.user
    instance = get_object_or_404(Setting, user=user)
    form = SettingUpdateForm(request.POST or None, instance=instance)
    
    if request.method == "POST":
        if form.is_valid():
            update_app = form.save(commit=False)
            dict = request.POST.dict()
            display_list = []
            for key, value in zip(dict.keys(), dict.values()):
                display_list.append((key,value))
            display_dict = {}
            for tuple in display_list[1:]:
                display_dict[tuple[0]] = tuple[1]
            update_app.display_list = json.dumps(display_dict)
            update_app.save()
            return redirect("home")
    context.update({
        'form': form
    })
    return render(request, 'settings.html', context)
