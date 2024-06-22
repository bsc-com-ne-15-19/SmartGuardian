# import logging
# from celery import shared_task
# from django.db.models import Count, Min, Max
# # from django.core.cache import cache
# from .models import AlertManager

# logger = logging.getLogger(__name__)

# @shared_task
# def aggregate_alert_data():
#     logger.info("Starting the aggregation task.")
    
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

#     # cache.set('aggregated_alert_data',str(frontend_data), timeout=60)
    
#     logger.info("Finished setting cache with aggregated data.")

#     return frontend_data



# import logging
# from celery import shared_task
# from django.db.models import Count, Min, Max
# from .models import AlertManager
# from datetime import timedelta  

# logger = logging.getLogger(__name__)

# @shared_task
# def aggregate_alert_data():
#     logger.info("Starting the aggregation task.")
    
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
#         # Fetch all alerts for each phone_number and student_name combination
#         all_alerts = AlertManager.objects.filter(
#             phone_number=alert['phone_number'],
#             student_name=alert['student_name']
#         ).order_by('timestamp')

#         # Group alerts based on the occurrence pattern
#         grouped_alerts = group_alerts_by_pattern(all_alerts)

#         # Prepare the data for each group
#         for group in grouped_alerts:
#             first_alert = group[0]
#             latest_alert = group[-1]
#             alert_status = 'Notified' if latest_alert.notified else 'Not Notified'
#             alert_count = len(group)

#             frontend_data.append({
#                 'phone_number': first_alert.phone_number.phone_number,
#                 'student_name': alert['student_name'],
#                 'timestamp': first_alert.timestamp,
#                 'alert_status': alert_status,
#                 'alert_count': alert_count,
#                 'location': latest_alert.location,
#             })
    
#     # Update the cache
#     cache.set('aggregated_alert_data', frontend_data, timeout=60)
#     logger.info("Finished setting cache with aggregated data.")
    
#     return frontend_data

# def group_alerts_by_pattern(alerts, time_delta=timedelta(hours=1)):
#     grouped_alerts = []
#     current_group = []

#     for alert in alerts:
#         if not current_group:
#             current_group.append(alert)
#         else:
#             if alert.timestamp - current_group[-1].timestamp <= time_delta:
#                 current_group.append(alert)
#             else:
#                 grouped_alerts.append(current_group)
#                 current_group = [alert]

#     if current_group:
#         grouped_alerts.append(current_group)

#     return grouped_alerts



import logging
from celery import shared_task
from django.db.models import Count, Min, Max
from .models import AlertManager
from datetime import timedelta  # Add this import
from django.core.cache import cache  # Add this import

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
        # Fetch all alerts for each phone_number and student_name combination
        all_alerts = AlertManager.objects.filter(
            phone_number=alert['phone_number'],
            student_name=alert['student_name']
        ).order_by('timestamp')

        # Group alerts based on the occurrence pattern
        grouped_alerts = group_alerts_by_pattern(all_alerts)

        # Prepare the data for each group
        for group in grouped_alerts:
            first_alert = group[0]
            latest_alert = group[-1]
            alert_status = 'Notified' if latest_alert.notified else 'Not Notified'
            alert_count = len(group)

            frontend_data.append({
                'phone_number': first_alert.phone_number.phone_number,
                'student_name': alert['student_name'],
                'timestamp': first_alert.timestamp,
                'alert_status': alert_status,
                'alert_count': alert_count,
                'location': latest_alert.location,
            })
    
    # Update the cache
    cache.set('aggregated_alert_data', frontend_data, timeout=60)
    logger.info("Finished setting cache with aggregated data.")
    
    return frontend_data

def group_alerts_by_pattern(alerts, time_delta=timedelta(hours=1)):
    grouped_alerts = []
    current_group = []

    for alert in alerts:
        if not current_group:
            current_group.append(alert)
        else:
            if alert.timestamp - current_group[-1].timestamp <= time_delta:
                current_group.append(alert)
            else:
                grouped_alerts.append(current_group)
                current_group = [alert]

    if current_group:
        grouped_alerts.append(current_group)

    return grouped_alerts
