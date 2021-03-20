from django.db import models

# Create your models here.

class SensorUnit(models.Model):
    latitude = models.DecimalField(max_digits=14,decimal_places=10, default=0)
    longitude = models.DecimalField(max_digits=14,decimal_places=10, default=0)
