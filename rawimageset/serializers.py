from rest_framework import serializers
from .models import RawImageSet 

class RawImageSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = RawImageSet 
        fields = ('id', 'field', 'date', 'file_path')