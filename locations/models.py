from django.db import models


class LocationWeather(models.Model):
    """
    We create a model but this could be acheieved without one.
    Done for the sake of completeness.
    """
    location = models.CharField(max_length=64)
    number_of_days = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    created = models.DateTimeField(
        auto_now_add=True, auto_now=True, blank=True)
    maximum = models.DecimalField(max_digits=5, decimal_places=2)
    minimum = models.DecimalField(max_digits=5, decimal_places=2)
    average = models.DecimalField(max_digits=5, decimal_places=2)
    median = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.location} - {self.start_date} - {self.end_date}"
