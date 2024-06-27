from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache
from .tasks import aggregate_alert_data
from .serializers import AlertManagerSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class AlertSummaryView(APIView):
    """
    API view for retrieving the summary of aggregated alert data.

    This view fetches the aggregated alert data from the cache and returns it as a response.
    If the cache is empty, it triggers the aggregation task to generate the data and stores it in the cache.

    Methods:
        - get: Retrieves the aggregated alert data from the cache or triggers the aggregation task if the cache is empty.
    """

    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Retrieves the aggregated alert data from the cache or triggers the aggregation task if the cache is empty.

        Returns:
            Response: The serialized aggregated alert data as a response.
        """
        # Fetch the cached data
        frontend_data = cache.get('aggregated_alert_data')

        if not frontend_data:
            # If cache is empty, trigger the aggregation task
            frontend_data = aggregate_alert_data()
            # Optionally, you can set the cache here to ensure it's updated immediately
            cache.set('aggregated_alert_data', frontend_data, timeout=60)

        serializer = AlertManagerSerializer(frontend_data, many=True)
        return Response(serializer.data)

# It uses Django Rest Framework and cache to efficiently handle the data retrieval and aggregation process.
