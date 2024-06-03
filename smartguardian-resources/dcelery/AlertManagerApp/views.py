# from django.shortcuts import render

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.db.models import Count
# from .models import AlertManager
# from .serializers import AlertManagerSerializer
# # Create your views here.

# class AlertSummaryView(APIView):
#     def get(self, request):
#         alerts = AlertManager.objects.values(
#             'phone_number',
#             'student_name',
#             'alert_started',
#             'alert_stopped',
#             'location'
#         ).annotate(
#             alert_count=Count('id')
#         ).order_by('-alert_count')
        
#         for alert in alerts:
#             alert['alert_status'] = 'Ongoing' if alert['alert_stopped'] is None else 'Stopped'

#         serializer = AlertManagerSerializer(alerts, many=True)
#         return Response(serializer.data)

# alerts/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
from .models import AlertManager
from .serializers import AlertManagerSerializer

class AlertSummaryView(APIView):
    def get(self, request):
        alerts = AlertManager.objects.annotate(
            alert_count=Count('id')
        ).order_by('-alert_count')
        
        serializer = AlertManagerSerializer(alerts, many=True)
        return Response(serializer.data)
