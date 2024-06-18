import logging
from celery import shared_task
from django.db.models import Count, Min, Max
# from django.core.cache import cache
from .models import AlertManager

logger = logging.getLogger(__name__)

@shared_task
def aggregate_alert_data():
    logger.info("Starting the aggregation task.")
    
    # Query to aggregate data based on phone_number and student_name
    alerts = AlertManager.objects.values(
        'phone_number', 'student_name'
    ).annotate(
        start_time=Min('timestamp'),
        alert_count=Count('id'),
        latest_latitude=Max('latitude'),
        latest_longitude=Max('longitude'),
    ).order_by('phone_number', 'student_name')

    frontend_data = []
    
    for alert in alerts:
        # Fetch latest alert for each phone_number and student_name combination
        latest_alert = AlertManager.objects.filter(
            phone_number=alert['phone_number'],
            student_name=alert['student_name']
        ).order_by('-timestamp').first()

        # Prepare the data according to the specified fields
        frontend_data.append({
            'phone_number': latest_alert.phone_number.phone_number,
            'student_name': alert['student_name'],
            'timestamp': alert['start_time'],
            'alert_status': 'Notified' if latest_alert.notified else 'Not Notified',
            'alert_count': alert['alert_count'],
            'location': latest_alert.location,
        })

    # cache.set('aggregated_alert_data',str(frontend_data), timeout=60)
    
    logger.info("Finished setting cache with aggregated data.")

    return frontend_data


# import logging
# from celery import shared_task
# from django.core.cache import cache
# from .models import AlertManager
# from django.db.models import Count, Min, Max

# logger = logging.getLogger(__name__)

# @shared_task
# def update_cache_with_alert_data_async(alert_id=None):
#     if alert_id:
#         try:
#             instance = AlertManager.objects.get(id=alert_id)
#             update_cache_with_alert_data(instance)
#         except AlertManager.DoesNotExist:
#             logger.warning(f"AlertManager instance with id {alert_id} does not exist.")
#     else:
#         update_cache_with_alert_data()

# def update_cache_with_alert_data(instance=None):
#     logger.info("Updating cache with new alert data.")

#     # Query to aggregate data based on phone_number and student_name
#     alerts = AlertManager.objects.values(
#         'phone_number', 'student_name'
#     ).annotate(
#         start_time=Min('timestamp'),
#         alert_count=Count('id'),
#         latest_latitude=Max('latitude'),
#         latest_longitude=Max('longitude'),
#     ).order_by('phone_number', 'student_name')

#     frontend_data = []
    
#     for alert in alerts:
#         # Fetch latest alert for each phone_number and student_name combination
#         latest_alert = AlertManager.objects.filter(
#             phone_number=alert['phone_number'],
#             student_name=alert['student_name']
#         ).order_by('-timestamp').first()

#         # Prepare the data according to the specified fields
#         frontend_data.append({
#             'phone_number': latest_alert.phone_number.phone_number,
#             'student_name': alert['student_name'],
#             'timestamp': alert['start_time'],
#             'alert_status': 'Notified' if latest_alert.notified else 'Not Notified',
#             'alert_count': alert['alert_count'],
#             'location': latest_alert.location,
#         })

#     cache.set('aggregated_alert_data', frontend_data, timeout=60*60)  # Cache for 1 hour
#     logger.info("Finished setting cache with aggregated data.")
    
    
#     return frontend_data
    
