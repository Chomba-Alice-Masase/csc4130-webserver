from django.urls import path, include

from .views import SensorDataCreateAPIView, SensorDataListAPIView, TempView, LatestTemperatureData

urlpatterns = [
    path('sensor-data/', SensorDataListAPIView.as_view(), name='sensor-data-list'),
    path('sensor-data/create/', SensorDataCreateAPIView.as_view(), name='sensor-data-create'),
    path('', TempView.as_view(), name='home'),
    path('latest-temperature-data/', LatestTemperatureData.as_view(), name='latest-temperature-data'),

]

