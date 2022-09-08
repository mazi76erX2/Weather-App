from datetime import datetime, timedelta
from statistics import median

from .models import LocationWeather
from .serializers import LocationWeatherSerializer

from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

import requests


class LocationWeatherView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LocationWeatherSerializer
    lookup_field = 'location'

    def get_location_forecast(self, location, number_of_days):
        """
        Using the location and days make an API request that returns average, median, max and min temperatures in
        Celsius in the given time period.
        """
        url = f'{settings.API_BASE_URL}{settings.API_KEY}&q={location}&days={number_of_days}&aqi=no&alerts=no'
        start_date = datetime.now()
        end_date = datetime.now() + timedelta(days=int(number_of_days))

        response = requests.get(url)
        status_code = response.status_code
        data_response = {"status_code": response.status_code}

        if status_code == 200:
            data = response.json()
            forecast = data['forecast']['forecastday']
            temperatures_min = [day['day']['mintemp_c'] for day in forecast]
            temperatures_max = [day['day']['maxtemp_c'] for day in forecast]
            temperatures_avg = [day['day']['avgtemp_c'] for day in forecast]

            maximum = max(temperatures_max)
            minimum = min(temperatures_min)
            average = sum(temperatures_avg) / len(temperatures_avg)
            median_temp = median(temperatures_avg)

            location_weather = LocationWeather.objects.create(
                location=location,
                number_of_days=number_of_days,
                start_date=start_date,
                end_date=end_date,
                maximum=maximum,
                minimum=minimum,
                average=average,
                median=median_temp,
            )

            location_weather = {
                "maximum": location_weather.maximum,
                "minimum": location_weather.minimum,
                "average": location_weather.average,
                "median": location_weather.median,
            }

            data_response.update({
                "message": "success",
                "data": location_weather
            })
        else:
            data_response.update({
                "message": response.json()['error']['message'],
                "data": {}
            })

        return data_response

    def get(self, request, location, format=None):
        days = self.request.query_params.get('days')

        if (int(days) > 13) or (int(days) < 1):
            # While testing I found that the API only returns data for 13 days.
            return Response({"error": "Invalid number of days", "status_code": status.HTTP_400_BAD_REQUEST})
        else:
            forecast_data = self.get_location_forecast(location, days)

            if forecast_data['status_code'] == 200:
                return Response(forecast_data['data'])
            else:
                return Response({"error": forecast_data['message'], "status_code": forecast_data['status_code']})
