# myapp/views.py

from rest_framework import generics
from .models import SensorData
from .serializers import SensorDataSerializer
from django.views import View


class SensorDataCreateAPIView(generics.CreateAPIView):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer


class SensorDataListAPIView(generics.ListAPIView):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer


class TempView(View):
    template_name = 'home.html'
