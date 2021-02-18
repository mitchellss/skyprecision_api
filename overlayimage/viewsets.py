from .models import OverlayImage
from field.models import Field
from index.models import Index
from stackedimage.models import StackedImage
from .serializers import OverlayImageSerializer 
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .file_utils import get_coordinates_from_tif

class OverlayImageViewset(viewsets.GenericViewSet):

    queryset = OverlayImage.objects.all()
    serializer_class = OverlayImageSerializer

    def list(self, request):
        # If superuser, display all objects
        if (request.user.is_superuser):
            queryset = OverlayImage.objects.all().order_by('date')
        # Else, only display user's objects
        else:
            queryset = OverlayImage.objects.filter(user=request.user.id).order_by('date')

        serializer = OverlayImageSerializer(queryset, many=True, context={'request' : request})
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = OverlayImage.objects.all()
        geonote = get_object_or_404(queryset, pk=pk)
        serializer = OverlayImageSerializer(geonote, context={'request' : request})
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        coordinates = get_coordinates_from_tif(f"{request.data['image_filename']}.tif")
        print(coordinates)

        data._mutable = True
        data['lat_2'] = coordinates[0]
        data['lat_1'] = coordinates[1]
        data['lon_1'] = coordinates[2]
        data['lon_2'] = coordinates[3]
        data._mutable = False


        serializer = OverlayImageSerializer(data=data, context={'request' : request})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    '''
    @action(methods=['get'], detail=False)
    def request_overlay(self, request, pk=None):
        data = request.data

        filtered_overlay_set = self.get_queryset().filter(
            field=data['field'], 
            date=data['date'], 
            file_path=data['file_path'], 
            tiff_file_path=data['tiff_file_path'], 
            scale_file_path=data['scale_file_path']
        )

        filtered_stacked_set = StackedImage.objects.filter(
            field=data['field'], 
            date=data['date'] 
        )

        if filtered_overlay_set:
            # There's an overlay that meets the specifications
            print('ay')
        elif filtered_stacked_set:
            # No overlay but there's a stacked image that meets the specifications
            print('doo')
        else:
            # There are no overlays or stacked images that meet the specifications
            return JsonResponse({'error' : 'no overlays or stacked images that meet specifications',
            'found' : False }, status=404) 

        return JsonResponse({'status' : 'goob'}, status=201)
        '''
