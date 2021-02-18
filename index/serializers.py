from rest_framework import serializers
from .models import Index

class IndexSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Index
        fields = ('name', 'long_name', 'summary')