from django.db import models
from DeviceApp.models import PhoneNumbers
import geocoder
from django.conf import settings
# import osmnx as ox


class AlertManager(models.Model):
    """
    Model representing an alert manager.

    Attributes:
        phone_number (ForeignKey): The phone number associated with the alert.
        student_name (CharField): The name of the student.
        location (CharField): The location of the alert.
        latitude (DecimalField): The latitude coordinate of the alert.
        longitude (DecimalField): The longitude coordinate of the alert.
        timestamp (DateTimeField): The timestamp when the alert was created.
        notified (BooleanField): Indicates if the alert has been notified.

    Meta:
        unique_together (tuple): Specifies that the combination of phone_number and timestamp should be unique.
    """

    phone_number = models.ForeignKey(PhoneNumbers, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    location = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    notified = models.BooleanField(default=False)

    class Meta:
        unique_together = ('phone_number', 'timestamp',)

    def save(self, *args, **kwargs):
        """
        Overrides the save method to update the location based on latitude and longitude.

        If latitude and longitude are provided, it uses the Mapbox API to reverse geocode the coordinates
        and update the location attribute.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            None
        """
        if self.latitude is not None and self.longitude is not None:
            g = geocoder.mapbox([self.latitude, self.longitude], method='reverse', key=settings.MAPBOX_API_KEY)
            if g.ok:
                self.location = g.address
        super(AlertManager, self).save(*args, **kwargs)
