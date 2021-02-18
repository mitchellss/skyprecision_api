from field.viewsets import FieldViewset
from geonote.viewsets import GeoNoteViewset
from rawimageset.viewsets import RawImageSetViewset
from overlayimage.viewsets import OverlayImageViewset
from stackedimage.viewsets import StackedImageViewset
from index.viewsets import IndexViewset
from customuser.viewsets import UserViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('field', FieldViewset, basename='field')
router.register('geonote', GeoNoteViewset, basename='geonote')
router.register('rawimageset', RawImageSetViewset, basename='rawimageset')
router.register('overlayimage', OverlayImageViewset, basename='overlayimage')
router.register('stackedimage', StackedImageViewset, basename='stackedimage')
router.register('index', IndexViewset, basename='index')
router.register('user', UserViewset, basename='user')
