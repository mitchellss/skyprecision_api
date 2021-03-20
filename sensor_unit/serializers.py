from rest_framework import serializers
from .models import SensorUnit

class SensorUnitSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = SensorUnit
        fields = ('id', 'latitude', 'longitude')