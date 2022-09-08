from .views import LocationWeatherView

from django.urls import path


urlpatterns = [
    path('api/locations/<str:location>/',
         LocationWeatherView.as_view(), name="get-location-forecast"),
]
