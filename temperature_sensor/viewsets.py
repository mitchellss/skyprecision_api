from .models import TemperatureSensor
from .serializers import TemperatureSensorSerializer
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
import datetime

class TemperatureSensorViewset(viewsets.GenericViewSet):

    queryset = TemperatureSensor.objects.all()
    serializer_class = TemperatureSensorSerializer

    def list(self, request):
        queryset = TemperatureSensor.objects.all()
        serializer = TemperatureSensorSerializer(queryset, many=True, context={'request', request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.queryset 
        sensor_unit = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(sensor_unit, context={'request' : request})
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data, context={'request' : request})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    @action(detail=False)
    def live_data(self, request):
        # Queryset of temperature recordings that were made in the past "num" minutes from the time the request was made.
        # Use this for requesting live data
        recent_recordings = self.queryset.filter(time__gte=(datetime.datetime.today() - datetime.timedelta(0,int(request.query_params.get('num'))*60)).timestamp())\
            .order_by('time').reverse() # So the first index will always be the most recent recording
        serializer = self.serializer_class(recent_recordings, many=True, context={'request', request})
        return Response(serializer.data)

    @action(detail=False)
    def most_recent_data(self, request):
        # Queryset of temperature recordings that were made in the past "num" minutes from the most recently recorded data point
        # Use this for demos where data hasn't been collected in a while
        most_recent_recording_time = self.queryset.order_by('time').last().__dict__['time']
        recent_recordings = self.queryset.filter(time__gte=most_recent_recording_time - datetime.timedelta(0,int(request.query_params.get('num'))*60))\
            .order_by('time').reverse() # So the first index will always be the most recent recording
        serializer = self.serializer_class(recent_recordings, many=True, context={'request', request})
        return Response(serializer.data)
        

