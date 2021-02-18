from rest_framework import serializers
from .models import StackedImage 

class StackedImageSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = StackedImage 
        fields = ('id', 'field', 'date', 'file_path', 'dem_file_path')