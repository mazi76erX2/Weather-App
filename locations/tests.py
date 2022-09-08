from datetime import datetime, timedelta

from .models import LocationWeather

from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase


class LocationWeatherTestCase(TestCase):
    def setUp(self):
        self.location_weather = LocationWeather.objects.create(
            location="Johannesburg",
            number_of_days=5,
            start_date=datetime.now(),
            end_date=datetime.now() + timedelta(days=int(5)),
            maximum=30.1,
            minimum=20.1,
            average=25.1,
            median=26.1,
        )

    def test_model_string(self):
        self.assertTrue(isinstance(self.location_weather(), LocationWeather))
        self.assertEqual(
            self.location_weather().__unicode__(),
            f"{self.location_weather.location} - {self.location_weather.start_date} - {self.location_weather.end_date}")


class LocationWeatherTestCase(APITestCase):
    def setUp(self):
        self.number_of_days = 5
        self.location = 'Johannesburg'

    def tearDown(self):
        LocationWeather.objects.all().delete()

    def make_request(self):
        url = f"{reverse('get-location-forecast', kwargs={'location': self.location})}?days={self.number_of_days}"
        print(url)
        response = self.client.get(url, format='json')

        return response

    def make_request_200_status_code(self):
        response = self.make_request()
        response_dict_keys = {'maximum', 'minimum', 'average', 'median'}
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.keys(), response_dict_keys)
        self.assertEqual(LocationWeather.objects.count(), 1)

    def make_request_400_status_code(self):
        response = self.make_request()
        self.assertEqual(
            response.data['status_code'], status.HTTP_400_BAD_REQUEST)
        self.assertEqual(LocationWeather.objects.count(), 0)

    def test_object_created(self):
        """
        Given a correct location and correct number of days, an object should be created in the database.
        """
        self.make_request_200_status_code()
        location_weather = LocationWeather.objects.first()
        self.assertEqual(location_weather.location, 'Johannesburg')
        self.assertEqual(location_weather.number_of_days, 5)
        start_date = datetime.now().date()
        end_date = (datetime.now() + timedelta(days=int(5))).date()
        self.assertEqual(location_weather.start_date, start_date)
        self.assertEqual(location_weather.end_date, end_date)

    def test_api_returns_data_for_5_days(self):
        self.make_request_200_status_code()

    def test_number_of_days_less_than_1_gives_error(self):
        self.number_of_days = 0

        self.make_request_400_status_code()

    def test_number_of_days_more_than_13_gives_error(self):
        self.number_of_days = 14

        self.make_request_400_status_code()

    def test_api_returns_error_for_unknown_location(self):
        self.location = 'Johanburg'

        self.make_request_400_status_code()
