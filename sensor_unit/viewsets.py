from .models import SensorUnit
from .serializers import SensorUnitSerializer
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, response
from rest_framework import viewsets
from rest_framework.response import Response

class SensorUnitViewset(viewsets.GenericViewSet):
    
    queryset = SensorUnit.objects.all()
    serializer_class = SensorUnitSerializer

    def list(self, request):
        queryset = SensorUnit.objects.all() 
        serializer = SensorUnitSerializer(queryset, many=True, context={'request', request})
        print("Test")
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.queryset 
        sensor_unit = get_object_or_404(queryset, pk=pk)
        serializer = SensorUnitSerializer(sensor_unit, context={'request' : request})
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        serializer = SensorUnitSerializer(data=data, context={'request' : request})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
