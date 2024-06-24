import json
from channels.generic.websocket import AsyncWebsocketConsumer

class GPSConsumer(AsyncWebsocketConsumer):
    """
    WebSocket consumer for handling GPS location updates.

    This consumer handles the WebSocket connection and manages the sending
    of GPS location updates to clients.

    Attributes:
        channel_name (str): The unique channel name for the WebSocket connection.
    """

    async def connect(self):
        """
        Called when the WebSocket is handshaking as part of the connection process.

        Connects the client to the "location_updates" group.

        Raises:
            WebSocketClose: If the user is not authenticated, the WebSocket connection is rejected.
        """
        await self.accept()
        await self.channel_layer.group_add("location_updates", self.channel_name)

    async def disconnect(self, close_code):
        """
        Called when the WebSocket closes for any reason.

        Removes the client from the "location_updates" group.

        Args:
            close_code (int): The WebSocket close code.
        """
        await self.channel_layer.group_discard("location_updates", self.channel_name)

    async def location_update(self, event):
        """
        Called when a location_update event is received.

        Sends the location update data to the client.

        Args:
            event (dict): The location_update event data.
        """
        data = event["data"]
        await self.send(text_data=json.dumps(data))
