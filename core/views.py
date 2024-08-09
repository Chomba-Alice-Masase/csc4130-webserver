from django.shortcuts import render
from rest_framework import viewsets
from .models import SensorData
from .serializers import SensorDataSerializer


# Create your views here.
class SensorDataViewSet(viewsets.ModelViewSet):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer
