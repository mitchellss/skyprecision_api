from sensor_unit.viewsets import SensorUnitViewset
from temperature_sensor.viewsets import TemperatureSensorViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('sensor_unit', SensorUnitViewset, basename='sensor_unit')
router.register('temperature_sensor', TemperatureSensorViewset, basename='temperature_sensor')