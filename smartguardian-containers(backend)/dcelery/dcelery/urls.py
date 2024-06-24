from django.contrib import admin
from django.urls import path, include
from StudentManagerApp.views import ReactView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ReactView.as_view(), name="Student"),
    path('ManageStudents/', ReactView.as_view(), name="ManageStudents"),
    path('alert_api/', include('AlertManagerApp.urls')),
    path('login_api/', include('APIGateway.urls')),
]

"""
This module defines the URL patterns for the SmartGuardian application.

The urlpatterns list contains various paths that map to different views within the application.
These paths are used to handle incoming requests and direct them to the appropriate view functions.

- '/admin/': URL for the Django admin site.
- '/': URL for the ReactView view, which is associated with the 'Student' name.
- '/ManageStudents/': URL for the ReactView view, which is associated with the 'ManageStudents' name.
- '/alert_api/': URL for including the URL patterns from the 'AlertManagerApp.urls' module.
- '/login_api/': URL for including the URL patterns from the 'APIGateway.urls' module.
"""
