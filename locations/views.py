from .models import LocationWeather
from .serializers import LocationWeatherSerializer

from django.conf import settings
from django.shortcuts import get_object_or_404

from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions


class LocationWeatherView(RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = LocationWeatherSerializer
    lookup_field = 'location'

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj
