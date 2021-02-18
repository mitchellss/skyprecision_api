from rest_framework import serializers
from .models import OverlayImage

class OverlayImageSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = OverlayImage
        fields = '__all__' 