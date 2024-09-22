from django.urls import path
from .views import relay_control, TempView, SensorDataCreateAPIView, SensorDataListAPIView, LatestTemperatureData

urlpatterns = [
    path('sensor-data/', SensorDataListAPIView.as_view(), name='sensor-data-list'),
    path('sensor-data/create/', SensorDataCreateAPIView.as_view(), name='sensor-data-create'),
    path('', TempView.as_view(), name='home'),
    path('latest-temperature-data/', LatestTemperatureData.as_view(), name='latest-temperature-data'),
    path('relay-control/', relay_control, name='relay-control'),
]
