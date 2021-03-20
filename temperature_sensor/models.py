from django.db import models
from sensor_unit.models import SensorUnit

# Create your models here.

class TemperatureSensor(models.Model):
    sensor = models.ForeignKey(SensorUnit, on_delete=models.CASCADE)
    time = models.IntegerField()
    temperature = models.DecimalField(max_digits=6, decimal_places=1, default=20)
