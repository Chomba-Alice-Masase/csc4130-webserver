from django.urls import path, include

from .views import SensorDataCreateAPIView , SensorDataListAPIView

urlpatterns = [
    path('sensor-data/', SensorDataListAPIView.as_view(), name='sensor-data-list'),
    path('sensor-data/create/', SensorDataCreateAPIView.as_view(), name='sensor-data-create'),
]

