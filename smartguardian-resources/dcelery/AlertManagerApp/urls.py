from django.urls import path
from .views import AlertSummaryView

urlpatterns = [
    path('alert-summary/', AlertSummaryView.as_view(), name='alert-summary'),
]

"""
This module defines the URL patterns for the Alert Manager app.

Example usage:
    To access the alert summary page, navigate to '/alert-summary/'. This will render the alert summary page.
"""
