import json
from channels.generic.websocket import AsyncWebsocketConsumer

# class GPSConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         # Accept the WebSocket connection
#         await self.accept()

#         # Add the client to the "location_updates" group
#         await self.channel_layer.group_add("location_updates", self.channel_name)

#     async def disconnect(self, close_code):
#         # Remove the client from the group when disconnected
#         await self.channel_layer.group_discard("location_updates", self.channel_name)

#     async def receive(self, text_data):
#         # Handle incoming WebSocket messages (if needed)
#         pass

#     async def location_message(self, event):
#         # Send location data to the client
#         location_data = event["message"]
#         await self.send(text_data=json.dumps(location_data))
        

class GPSConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("location_updates", self.channel_name)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("location_updates", self.channel_name)

    async def location_update(self, event):
        data = event["data"]
        await self.send(text_data=json.dumps(data))
