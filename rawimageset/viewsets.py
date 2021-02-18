from field.models import Field
from .models import RawImageSet 
from .serializers import RawImageSerializer 
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.response import Response

class RawImageSetViewset(viewsets.GenericViewSet):
    
    queryset = RawImageSet.objects.all()
    serializer_class = RawImageSerializer

    def list(self, request):
        if (request.user.is_superuser):
            queryset = RawImageSet.objects.all()
        else:
            queryset = RawImageSet.objects.filter(user=request.user.id)

        serializer = RawImageSerializer(queryset, many=True, context={'request' : request})
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = RawImageSet.objects.all()
        geonote = get_object_or_404(queryset, pk=pk)
        serializer = RawImageSerializer(geonote, context={'request' : request})
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        serializer = RawImageSerializer(data=data, context={'request' : request})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)