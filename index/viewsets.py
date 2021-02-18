from .models import Index
from .serializers import IndexSerializer 
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.response import Response

class IndexViewset(viewsets.GenericViewSet):

    queryset = Index.objects.all()
    serializer_class = IndexSerializer

    def list(self, request):
        if (request.user.is_superuser):
            queryset = Index.objects.all()
        else:
            queryset = Index.objects.filter(user=request.user.id)

        serializer = IndexSerializer(queryset, many=True, context={'request' : request})
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Index.objects.all()
        index = get_object_or_404(queryset, pk=pk)
        serializer = IndexSerializer(index, context={'request' : request})
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        serializer = IndexSerializer(data=data, context={'request' : request})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)