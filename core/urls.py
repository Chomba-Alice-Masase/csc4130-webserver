from django.urls import path, include

from .views import SensorDataCreateAPIView, SensorDataListAPIView, TempView

urlpatterns = [
    path('sensor-data/', SensorDataListAPIView.as_view(), name='sensor-data-list'),
    path('sensor-data/create/', SensorDataCreateAPIView.as_view(), name='sensor-data-create'),
    path('', TempView.as_view(), name='home'),
]

