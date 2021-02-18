from .models import StackedImage
from field.models import Field
from .serializers import StackedImageSerializer 
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.response import Response

class StackedImageViewset(viewsets.GenericViewSet):

    queryset = StackedImage.objects.all()
    serializer_class = StackedImageSerializer

    def list(self, request):
        if request.user.is_superuser:
            queryset = StackedImage.objects.all()
        else:
            fields = Field.objects.filter(user=request.user)
            queryset = StackedImage.objects.filter(field__in=fields).prefetch_related()

        serializer = StackedImageSerializer(queryset, many=True, context={'request' : request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = StackedImage.objects.all()
        geonote = get_object_or_404(queryset, pk=pk)
        serializer = StackedImageSerializer(geonote, context={'request' : request})
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        serializer = StackedImageSerializer(data=data, context={'request' : request})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)