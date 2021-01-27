from api.models import Temperature
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import TemperatureSerializer
from rest_framework.response import Response
from django_filters import rest_framework as filters
from django_filters import DateTimeFromToRangeFilter


class TemperatureFilter(filters.FilterSet):
    date = DateTimeFromToRangeFilter()

    class Meta:
        model = Temperature
        fields = ['date']


class TemperatureViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows temperatures to be viewed and created.
    """
    queryset = Temperature.objects.all().order_by('date')
    serializer_class = TemperatureSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = TemperatureFilter


class NumericsViewSet(viewsets.ViewSet):
    """
    API endpoint that returns Numerics Custom JSON.
    """

    def list(self, request):
        queryset = Temperature.objects.all().order_by('-date')
        temperature1 = queryset[0].temperature
        temperature2 = queryset[1].temperature
        color = 'red'
        if temperature1 >= temperature2:
            color = 'green'
        return Response({
            'postfix': 'Temperature',
            'color': color,
            'data': [
                {
                    'value': temperature1
                },
                {
                    'value': temperature2
                }
            ]
        })
