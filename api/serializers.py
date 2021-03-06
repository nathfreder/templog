from rest_framework import serializers
from .models import Temperature
from .utils import round_temperature


class TemperatureField(serializers.Field):
    def to_representation(self, value):
        return round_temperature(value)

    def to_internal_value(self, data):
        return data


class TemperatureSerializer(serializers.ModelSerializer):
    temperature = TemperatureField()
    temperature_f = serializers.SerializerMethodField()

    class Meta:
        model = Temperature
        fields = ['id', 'temperature', 'temperature_f', 'date']

    def get_temperature_f(self, obj):
        return round_temperature((round_temperature(obj.temperature) * 1.8) + 32)
