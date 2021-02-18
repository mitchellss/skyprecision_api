from .models import Field
from .serializers import FieldSerializer
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.response import Response


class FieldViewset(viewsets.GenericViewSet):

    queryset = Field.objects.all()
    serializer_class = FieldSerializer

    def list(self, request):
        if (request.user.is_superuser):
            queryset = Field.objects.all()
        else:
            queryset = Field.objects.filter(user=request.user.id)

        serializer = FieldSerializer(queryset, many=True, context={'request' : request})
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Field.objects.all()
        field = get_object_or_404(queryset, pk=pk)
        serializer = FieldSerializer(field, context={'request' : request})
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        serializer = FieldSerializer(data=data, context={'request' : request})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)