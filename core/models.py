from django.db import models


# Create your models here.


class SensorData(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField(default=0.0)  # New field to store humidity
