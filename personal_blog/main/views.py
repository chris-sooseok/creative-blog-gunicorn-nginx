from django.core.checks import messages
from django.shortcuts import get_object_or_404, render, redirect
import requests
from .models import City, Setting
from django.contrib.auth.decorators import login_required
from .forms import SettingUpdateForm
import json
from config.settings import DISPLAY_APPS
# Create your views here.


# home page
def MainListFunction(request):
    # list of recent posts
    # list of weather
    context = {}
    if request.user.is_authenticated:
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&units={}&appid=96748c1eb3fe471926e26a21bafd6c4e"

        cities = City.objects.filter(user=request.user).all()

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

        cities = City.objects.filter(user=request.user).all()
        setting = Setting.objects.get(user=request.user)
        
           
        context.update({"cities": cities, "message": message, "setting": setting})
    else:
        pass

    return render(request, '_home.html', context)

# create weather on home page
@login_required
def WeatherCreateFunction(request):
    if request.user.is_authenticated:
        city_name_list = request.POST['city'].split(" ")
        city_name_list = [word for word in city_name_list if word != ""]
        city_name = " ".join(map(str,city_name_list))
        City(user=request.user, name=city_name.title()).save()

        return redirect('home')
    else:
        return redirect('account_login')
# delete weather on home page
@login_required
def WeatherDeleteFunction(request, pk):
    if request.user.is_authenticated:
        city_name = City.objects.get(user=request.user, id=pk)
        city_name.delete()
        return redirect('home')
    else:
        return redirect('account_login')

# update setting on home page
@login_required
def SettingUpdateFunction(request):
    context = {}
    user = request.user
    instance = get_object_or_404(Setting, user=user)

    # App
    form = SettingUpdateForm(request.POST or None, request.FILES or None, instance=instance)
  
    if request.method == "POST":
        if form.is_valid():
            update_app = form.save(commit=False)
            dict = request.POST.dict()
            display_dict = {}
            for key, value in zip(dict.keys(), dict.values()):
                if key in DISPLAY_APPS:
                    if value == "True":
                        display_dict[key] = True
                    else:
                        display_dict[key] = False
            update_app.app_display_dict = json.dumps(display_dict)
            update_app.save()
            return redirect("home")
    context.update({
        'appupdateform': form
    })
    return render(request, 'settings.html', context)
