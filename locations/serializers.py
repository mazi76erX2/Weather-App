from rest_framework import serializers
from .models import LocationWeather


class LocationWeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationWeather
        fields = ['locations', 'days', 'maximum',
                  'minimum', 'average', 'median']
