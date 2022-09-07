from django.urls import path
from .views import LocationWeatherView


urlpatterns = [
    path('api/locations/<str:location>/?days=<int:number_of_days>', LocationWeatherView.as_view(), name="get_location_details"),
]
