import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class TemperatureConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        # Process incoming messages if needed
        text_data_json = json.loads(text_data)
        temperature = text_data_json['temperature']

        # Send message back to the WebSocket
        self.send(text_data=json.dumps({
            'temperature': temperature
        }))
