from django.db import models
from customuser.models import User

class Field(models.Model):
    name = models.CharField(max_length=60, default='')
    user = models.ManyToManyField(User)
    latitude = models.DecimalField(max_digits=14,decimal_places=10,default=0)
    longitude = models.DecimalField(max_digits=14,decimal_places=10, default=0)
    def __str__(self):
        return self.name