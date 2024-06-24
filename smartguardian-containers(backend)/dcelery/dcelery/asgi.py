import os
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dcelery.settings')

# Get the Django ASGI application
django_application = get_asgi_application()

# Import the websocket URL patterns
from APIGateway.routing import websocket_urlpatterns

# Create the ASGI application
application = ProtocolTypeRouter({
    "http": django_application,
    "websocket": AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns)
    ),
})

"""
ASGI configuration for dcelery project.

This module configures the ASGI (Asynchronous Server Gateway Interface) for the dcelery project.
It sets the Django settings module, gets the Django ASGI application, and creates the ASGI application
with support for both HTTP and WebSocket protocols.

The ASGI application is created using the ProtocolTypeRouter, which routes HTTP requests to the Django
application and WebSocket requests to the AuthMiddlewareStack with the URLRouter.

For more information on ASGI, see: https://asgi.readthedocs.io/
"""
