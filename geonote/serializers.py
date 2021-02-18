from rest_framework import serializers
from .models import GeoNote

class GeoNoteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = GeoNote
        fields = ('id', 'user', 'field', 'date', 'latitude', 'longitude', 'value')