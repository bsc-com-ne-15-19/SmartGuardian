from django.urls import re_path
from .consumers import GPSConsumer

websocket_urlpatterns = [
    re_path(r"ws/location_updates/$", GPSConsumer.as_asgi()),
]