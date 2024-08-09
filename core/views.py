# myapp/views.py

from rest_framework import generics
from .models import SensorData
from .serializers import SensorDataSerializer


class SensorDataCreateAPIView(generics.CreateAPIView):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer


class SensorDataListAPIView(generics.ListAPIView):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer
