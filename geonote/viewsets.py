from .models import GeoNote, Field
from .serializers import GeoNoteSerializer 
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.response import Response

class GeoNoteViewset(viewsets.GenericViewSet):

    queryset = GeoNote.objects.all()
    serializer_class = GeoNoteSerializer

    def list(self, request):
        if (request.user.is_superuser):
            queryset = GeoNote.objects.all()
        else:
            queryset = GeoNote.objects.filter(user=request.user.id)

        serializer = GeoNoteSerializer(queryset, many=True, context={'request' : request})
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = GeoNote.objects.all()
        geonote = get_object_or_404(queryset, pk=pk)
        serializer = GeoNoteSerializer(geonote, context={'request' : request})
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        serializer = GeoNoteSerializer(data=data, context={'request' : request})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)