from django.urls import path
from .views import MainListFunction, WeatherCreateFunction, WeatherDeleteFunction, AppUpdateFunction

urlpatterns = [
    path('', MainListFunction, name='home'),
    path('craete_weather/', WeatherCreateFunction, name='create_weather'),
    path('<uuid:pk>/', WeatherDeleteFunction, name="delete_weather"),
    path('settings/', AppUpdateFunction, name="update_setting"),
]