# # myapp/signals.py
# from django.db.models.signals import post_save, post_delete
# from django.dispatch import receiver
# from .models import AlertManager
# from django.core.cache import cache
# from .tasks import aggregate_alert_data  # Import your Celery task

# @receiver(post_save, sender=AlertManager)
# @receiver(post_delete, sender=AlertManager)
# def update_aggregated_alert_data(sender, instance, **kwargs):
#     # Trigger the aggregation task whenever AlertManager instances are saved or deleted
#     aggregate_alert_data.delay()

# # @receiver(post_delete, sender=AlertManager)
# # def alert_manager_deleted(sender, instance, **kwargs):
# #     update_cache_with_alert_data_async.delay(instance.id)

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import AlertManager
from .tasks import aggregate_alert_data

@receiver(post_save, sender=AlertManager)
@receiver(post_delete, sender=AlertManager)
def update_aggregated_alert_data(sender, instance, **kwargs):
    aggregate_alert_data.delay()
