from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Sensor, TemperatureMeasurement
from .serializers import SensorSerializer, TemperatureMeasurementSerializer
from rest_framework import status

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    @action(detail=True, methods=['post'])
    def add_measurement(self, request, pk=None):
        sensor = self.get_object()
        temperature = request.data.get('temperature')

        if temperature is None:
            return Response({"detail": "Temperature is required."}, status=status.HTTP_400_BAD_REQUEST)

        measurement = TemperatureMeasurement.objects.create(sensor=sensor, temperature=temperature)
        measurement_serializer = TemperatureMeasurementSerializer(measurement)

        return Response(measurement_serializer.data, status=status.HTTP_201_CREATED)
