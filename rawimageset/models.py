from django.db import models
from field.models import Field

# Create your models here.
class RawImageSet(models.Model):
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False)
    file_path = models.CharField(max_length=100)