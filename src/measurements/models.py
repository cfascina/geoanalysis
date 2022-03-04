from statistics import mode
from django.db import models

class Measurements(models.Model):
    location = models.CharField(max_length = 200)
    point_from = models.CharField(max_length = 200)
    destination = models.CharField(max_length = 200)
    point_to = models.CharField(max_length = 200)
    distance = models.DecimalField(max_digits = 10, decimal_places = 2)
    createad = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"Distance from {self.location} to  {self.destination} is {self.distance} km"
