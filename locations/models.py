from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class LocationWeather(models.Model):
    """
    We create a model but this could be acheieved without one.
    Done for the sake of completeness. It allows us to standardise the information we are returning.
    And validation.
    """
    location = models.CharField(max_length=64)
    number_of_days = models.PositiveSmallIntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(13)])
    start_date = models.DateField()
    end_date = models.DateField()
    created = models.DateTimeField(auto_now_add=True, blank=True)
    maximum = models.DecimalField(max_digits=3, decimal_places=1)
    minimum = models.DecimalField(max_digits=3, decimal_places=1)
    average = models.DecimalField(max_digits=4, decimal_places=2)
    median = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.location} - {self.start_date} - {self.end_date}"
