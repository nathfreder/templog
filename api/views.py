from api.models import Temperature
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import TemperatureSerializer


class TemperatureViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows temperatures to be viewed and created.
    """
    queryset = Temperature.objects.all().order_by('date')
    serializer_class = TemperatureSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]