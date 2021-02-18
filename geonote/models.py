from django.db import models
from customuser.models import User
from field.models import Field 

class GeoNote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    latitude = models.DecimalField(max_digits=14,decimal_places=10,default=0)
    longitude = models.DecimalField(max_digits=14,decimal_places=10, default=0)
    value =  models.CharField(max_length=60)

    def __str__(self):
        return self.value