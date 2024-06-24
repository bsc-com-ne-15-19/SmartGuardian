from django.urls import path
from .views import LoginAPIView

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
]
"""
This module defines the URL patterns for the API Gateway, which serves as the entry point for the API endpoints.
URL Patterns:
- /login/ : Maps to the LoginAPIView class-based view for user authentication.

"""
