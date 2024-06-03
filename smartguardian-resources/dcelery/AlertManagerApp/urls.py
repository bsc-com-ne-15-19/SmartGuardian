from django.urls import path
from .views import AlertSummaryView

urlpatterns = [
    path('alert-summary/', AlertSummaryView.as_view(), name='alert-summary'),
]
