from datetime import datetime, timedelta
from django.test import TestCase
from .models import LocationWeather


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

    def test_number_of_days_less_than_1_gives_error(self):
        pass

    def test_number_of_days_more_than_14_gives_error(self):
        pass

    def test_api_returns_status_code_200_for_5_days(self):
        pass

    def test_api_returns_data_for_5_days(self):
        pass

    def test_api_returns_error_for_unknown_location(self):
        pass
