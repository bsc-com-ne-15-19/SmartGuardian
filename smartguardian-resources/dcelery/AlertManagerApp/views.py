# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.core.cache import cache
# from .tasks import aggregate_alert_data
# from .serializers import AlertManagerSerializer
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.permissions import IsAuthenticated

# class AlertSummaryView(APIView):
#     # authentication_classes = [JWTAuthentication]
#     # permission_classes = [IsAuthenticated]

#     def get(self, request):
#         # Fetch the cached data
#         frontend_data = cache.get('aggregated_alert_data')

#         if not frontend_data:
#             # If cache is empty, trigger the aggregation task
#             frontend_data = aggregate_alert_data()
#             # Optionally, you can set the cache here to ensure it's updated immediately
#             cache.set('aggregated_alert_data', frontend_data, timeout=60)

#         serializer = AlertManagerSerializer(frontend_data, many=True)
#         return Response(serializer.data)
 
 
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.core.cache import cache
# from .tasks import aggregate_alert_data
# from .serializers import AlertManagerSerializer
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.permissions import IsAuthenticated

# class AlertSummaryView(APIView):
#     # authentication_classes = [JWTAuthentication]
#     # permission_classes = [IsAuthenticated]

#     def get(self, request):
#         # Fetch the cached data
#         frontend_data = cache.get('aggregated_alert_data')

#         if not frontend_data:
#             # If cache is empty, trigger the aggregation task
#             frontend_data = aggregate_alert_data()
#             # Optionally, you can set the cache here to ensure it's updated immediately
#             cache.set('aggregated_alert_data', frontend_data, timeout=60)

#         serializer = AlertManagerSerializer(frontend_data, many=True)
#         return Response(serializer.data)

from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache
from .tasks import aggregate_alert_data
from .serializers import AlertManagerSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class AlertSummaryView(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        # Fetch the cached data
        frontend_data = cache.get('aggregated_alert_data')

        if not frontend_data:
            # If cache is empty, trigger the aggregation task
            frontend_data = aggregate_alert_data()
            # Optionally, you can set the cache here to ensure it's updated immediately
            cache.set('aggregated_alert_data', frontend_data, timeout=60)

        serializer = AlertManagerSerializer(frontend_data, many=True)
        return Response(serializer.data)

        
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.core.cache import cache
# from .tasks import aggregate_alert_data
# from .serializers import AlertManagerSerializer
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.permissions import IsAuthenticated

# class AlertSummaryView(APIView):
#     # authentication_classes = [JWTAuthentication]
#     # permission_classes = [IsAuthenticated]

    
#     def get(self, request):
#         # Fetch the cached data
#         frontend_data = aggregate_alert_data()
#         # cache.get('aggregated_alert_data')

#         if not frontend_data:
#             # If cache is empty, trigger the aggregation task
#             aggregate_alert_data.delay()
#             frontend_data = []
#             # print(f"\n\n\n\n{frontend_data}\n\n\n\n")


#         serializer = AlertManagerSerializer(frontend_data, many=True)
#         return Response(serializer.data)


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.core.cache import cache
# from .tasks import update_cache_with_alert_data_async
# from .serializers import AlertManagerSerializer

# class AlertSummaryView(APIView):
#     def get(self, request):
#         # Fetch the cached data
#         frontend_data = update_cache_with_alert_data_async()
#         if frontend_data is None:
#             # If cache is empty, trigger the aggregation task
#             update_cache_with_alert_data_async.delay()
#             return Response({"message": "Data is being prepared, please check back shortly."}, status=202)
#         elif not frontend_data:
#             print("Cached data is an empty list")

#         print(f"\n\n\n\nRetrieved frontend_data: {frontend_data}\n\n\n\n")

#         serializer = AlertManagerSerializer(frontend_data, many=True)
#         return Response(serializer.data)
