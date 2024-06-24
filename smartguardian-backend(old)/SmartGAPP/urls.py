from django.urls import path
from SmartGAPP import views

urlpatterns = [
    path('students/', views.Student_list, name='student_list'),
    path('students/<int:id>/', views.Student_list, name='student_detail'),
    path('emergency-alerts/', views.emergency_alert, name='emergency_alert_list'),
    path('emergency-alerts/<int:id>/', views.emergency_alert, name='emergency_alert_detail'),
    path('administrator-users/', views.administrator_user, name='administrator_user_list'),
    path('administrator-users/<str:employee_id>/', views.administrator_user, name='administrator_user_detail'),
    path('devices/', views.device_list, name='device_list'),
    path('devices/<int:phone_number>/', views.device_list, name='device_detail'),
    path('locations/', views.location_list, name='location_list'),
    path('locations/<str:location_id>/', views.location_list, name='location_detail'),
]