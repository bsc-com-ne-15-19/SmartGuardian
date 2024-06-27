from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import AlertManager
from .tasks import aggregate_alert_data

@receiver(post_save, sender=AlertManager)
@receiver(post_delete, sender=AlertManager)
def update_aggregated_alert_data(sender, instance, **kwargs):
    """
    Signal receiver function that updates the aggregated alert data.

    This function is triggered whenever a new AlertManager instance is saved or deleted.
    It calls the `aggregate_alert_data` task asynchronously to update the aggregated alert data.

    Args:
        sender: The sender of the signal.
        instance: The instance of AlertManager that triggered the signal.
        **kwargs: Additional keyword arguments.

    Returns:
        None
    """
    aggregate_alert_data.delay()

# This module contains signal receivers for the AlertManager model.
# These receivers are responsible for updating the aggregated alert data (e.g., alert counts)
# whenever a new AlertManager instance is saved or deleted.