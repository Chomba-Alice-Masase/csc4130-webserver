from django.db import models


# Create your models here.

class SensorData(models.Model):
    temperature = models.FloatField()
    timestamp = models.DateTimeField()
    date = models.DateField()

