from django.urls import re_path
from .consumers import GPSConsumer

websocket_urlpatterns = [
    re_path(r"ws/location_updates/$", GPSConsumer.as_asgi()),
]
"""
This module defines the routing configuration for the APIGateway application.

The `websocket_urlpatterns` list contains the URL patterns for WebSocket connections.
In this case, there is a single pattern defined: "ws/location_updates/".
When a WebSocket connection is made to this URL, the `GPSConsumer` class will handle the connection.

Note: This module is part of the SmartGuardian project and is located in the dcelery/APIGateway directory.
"""
