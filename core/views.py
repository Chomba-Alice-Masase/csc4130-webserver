from django.shortcuts import render
from rest_framework import generics
from .models import SensorData
from .serializers import SensorDataSerializer
from django.views import View
from django.http import JsonResponse


class SensorDataCreateAPIView(generics.CreateAPIView):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer


class SensorDataListAPIView(generics.ListAPIView):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer


class TempView(View):
    template_name = 'home.html'

    def get(self, request):
        sensor_data = SensorData.objects.all().order_by('-id')

        context = {'sensor_data': sensor_data}
        return render(request, self.template_name, context)

class LatestTemperatureData(View):
    def get(self, request):
        sensor_data = SensorData.objects.all().order_by('-id')[:10]  # Fetch last 10 readings
        data = list(sensor_data.values('temperature', 'id'))
        return JsonResponse(data, safe=False)