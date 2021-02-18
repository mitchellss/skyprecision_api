from django.db import models
from field.models import Field
from index.models import Index

# Create your models here.
class OverlayImage(models.Model):
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    index = models.ForeignKey(Index, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False)
    image_filename = models.CharField(max_length=100)
    scale_filename = models.CharField(max_length=100)
    lat_1 = models.FloatField(null=True)
    lat_2 = models.FloatField(null=True) 
    lon_1 = models.FloatField(null=True)
    lon_2 = models.FloatField(null=True)

    def __str__(self):
        return self.image_filename
