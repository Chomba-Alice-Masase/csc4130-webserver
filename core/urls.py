from django.urls import path, include

from .views import SensorDataCreateAPIView, SensorDataListAPIView, TempView

urlpatterns = [
    path('sensor-data/', SensorDataListAPIView.as_view(), name='sensor-data-list'),
    path('sensor-data/create/', SensorDataCreateAPIView.as_view(), name='sensor-data-create'),
    path('home', TempView.as_view(template_name='home.html'), name='home'),
]

