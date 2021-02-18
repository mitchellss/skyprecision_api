from rest_framework import serializers
from .models import Field

class FieldSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Field
        fields = ('id', 'name', 'user', 'latitude', 'longitude')