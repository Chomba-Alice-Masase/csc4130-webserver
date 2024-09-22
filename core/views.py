from django.shortcuts import render
from rest_framework import generics
from .models import SensorData
from .serializers import SensorDataSerializer
from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

# This file contains data regarding the views that make the API calls.

@method_decorator(csrf_exempt, name='dispatch')  # Apply csrf_exempt to the entire class
class SensorDataCreateAPIView(generics.CreateAPIView):  # This handles the post requests from the esp32
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer


class SensorDataListAPIView(generics.ListAPIView):  # This lists the posts through a get request
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer


class TempView(View):  # This is our home view for our web app.
    template_name = 'home.html'

    def get(self, request):
        sensor_data = SensorData.objects.all().order_by('-id')

        context = {'sensor_data': sensor_data}
        return render(request, self.template_name, context)


class LatestTemperatureData(View):  # This fetches the posted data and displays it on our webpage.
    def get(self, request):
        sensor_data = SensorData.objects.all().order_by('-id')[:10]  # Fetch last 10 readings
        data = list(sensor_data.values('temperature', 'humidity', 'id'))  # Include humidity in the data
        return JsonResponse(data, safe=False)


relay_state = "off"  # This will store the current relay state


@csrf_exempt
def relay_control(request):
    global relay_state

    if request.method == "GET":
        # Return the current state of the relay
        return JsonResponse({"relay": relay_state})

    elif request.method == "POST":
        # Change the state of the relay based on the client's request
        try:
            data = json.loads(request.body)
            new_state = data.get("relay")

            if new_state in ["on", "off"]:
                relay_state = new_state
                return JsonResponse({"relay": relay_state}, status=200)
            else:
                return JsonResponse({"error": "Invalid relay state"}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Bad request"}, status=400)
