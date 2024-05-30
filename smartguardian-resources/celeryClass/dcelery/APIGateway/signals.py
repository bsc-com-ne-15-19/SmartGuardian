from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from DeviceApp.models import LocationData

@receiver(post_save, sender=LocationData)
def send_location_update(sender, instance, **kwargs):
    channel_layer = get_channel_layer()
    group_name = "location_updates"
    
    data = {
        "phone_number": str( instance.phone_number.phone_number),  # Extract phone number as a string
        "student_name": str(instance.student_name),
        "latitude": str(instance.latitude),  # Convert Decimal to string for serialization
        "longitude": str(instance.longitude), 
        "alert": str(instance.alert),
    }
    try:
        async_to_sync(channel_layer.group_send)(
            group_name,
            {"type": "location_update", "data": data}
        )
    except Exception as e:
        # Handle or log the exception
        print(f"Error sending message: {e}")