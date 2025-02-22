from rest_framework import serializers
from .models import Sensor, TemperatureMeasurement

class TemperatureMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperatureMeasurement
        fields = ['temperature', 'created_at']

class SensorSerializer(serializers.ModelSerializer):
    measurements = TemperatureMeasurementSerializer(many=True, read_only=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
