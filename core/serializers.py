# Serializers are used to convert complex datatypes like django models into simple python datatypes like dictionaries
# This enables them to be easily rendered into JSON, XML, or other content type. It also allows the opposite
# This assists in sending data over the api
# In this case we are serializing the data from our sensors.

from rest_framework import serializers
from core.models import SensorData


class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = '__all__'

