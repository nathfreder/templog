from api.models import Temperature
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from .serializers import TemperatureSerializer
from rest_framework.response import Response
from django_filters import rest_framework as filters
from django_filters import DateTimeFromToRangeFilter
from api.utils import round_temperature


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

    @action(detail=False, methods=['get'], name='Get Latest Temperature')
    def latest(self, request):
        latest = Temperature.objects.latest('id')
        serializer = self.get_serializer(latest)
        return Response(serializer.data)


class NumericsViewSet(viewsets.ViewSet):
    """
    API endpoint that returns Numerics Custom JSON.
    """

    def list(self, request):
        queryset = Temperature.objects.all().order_by('-date')
        temperature1 = round_temperature(queryset[0].temperature)
        temperature2 = round_temperature(queryset[1].temperature)
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