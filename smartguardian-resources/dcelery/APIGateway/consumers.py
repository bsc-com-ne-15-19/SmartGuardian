import json
from channels.generic.websocket import AsyncWebsocketConsumer       

class GPSConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # # Check if the user is authenticated
        # if not self.scope["user"].is_authenticated:
        #     # Reject the WebSocket connection
        #     await self.close()
        # else:
        #     # Add the client to the "location_updates" group
        #     await self.channel_layer.group_add("location_updates", self.channel_name)
        await self.accept()
        await self.channel_layer.group_add("location_updates", self.channel_name)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("location_updates", self.channel_name)

    async def location_update(self, event):
        data = event["data"]
        await self.send(text_data=json.dumps(data))
