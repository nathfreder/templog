from django.shortcuts import render
from api.models import Temperature


def index(request):
    temperature = Temperature.objects.latest('date')
    return render(request, 'chart/index.html', {'temperature': round(temperature.temperature)})
