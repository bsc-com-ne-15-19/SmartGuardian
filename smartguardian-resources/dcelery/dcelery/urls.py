from django.contrib import admin
from django.urls import path
from StudentManagerApp.views import ReactView
# from APIGateway.consumers import GPSConsumer  # Import your consumers here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ReactView.as_view(), name="Student"),
    path('ManageStudents/', ReactView.as_view(), name="ManageStudents"),
]