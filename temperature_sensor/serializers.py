from rest_framework import serializers
from .models import TemperatureSensor

class TemperatureSensorSerializer(serializers.ModelSerializer):

    class Meta:
        model = TemperatureSensor
        fields = ('id', 'sensor', 'time', 'temperature')