from django.urls import path
from .views import LocationWeatherView


urlpatterns = [
    path('api/locations/<str:location>/',
         LocationWeatherView.as_view(), name="get-location-forecast"),
]
