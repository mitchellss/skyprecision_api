from django.db import models

# Create your models here.
class Index(models.Model):
    name = models.CharField(max_length=30)
    long_name = models.CharField(max_length=60, default=' ')
    summary = models.CharField(max_length=500, default=' ')

    def __str__(self):
        return self.name