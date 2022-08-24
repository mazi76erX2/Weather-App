from django.urls import path
from .views import LocationWeatherView


urlpatterns = [
    path('api/locations/<city:str>/?days=<number_of_days:int>', LocationWeatherView.as_view()),
]
