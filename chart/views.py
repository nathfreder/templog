from django.shortcuts import render
from api.models import Temperature
from api.utils import round_temperature


def index(request):
    temperature = Temperature.objects.latest('date')
    return render(request, 'chart/index.html', {'temperature': round_temperature(temperature.temperature)})
