# from django.db import models
# from DeviceApp.models import PhoneNumbers
# import geocoder
# from django.conf import settings


# # # Create your models here.
# class AlertManager(models.Model):
#     phone_number = models.ForeignKey(PhoneNumbers, on_delete=models.CASCADE)
#     student_name = models.CharField(max_length=100)
#     location = models.CharField(max_length=255, blank=True, null=True)
#     latitude = models.DecimalField(max_digits=9, decimal_places=6)
#     longitude = models.DecimalField(max_digits=9, decimal_places=6)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     alert_started = models.DateTimeField(null=True, blank=True)
#     alert_stopped = models.DateTimeField(null=True, blank=True)
#     notified = models.BooleanField(default=False)

#     class Meta:
#         unique_together = ('phone_number', 'timestamp',)

#     def save(self, *args, **kwargs):
#         if self.location:
#             g = geocoder.mapbox(self.location, key=settings.MAPBOX_API_KEY)
#             g = g.latlng
#             if g:
#                 self.latitude = g[0]
#                 self.longitude = g[1]
#         super(AlertManager, self).save(*args, **kwargs)
from django.db import models
from DeviceApp.models import PhoneNumbers
import geocoder
from django.conf import settings


class AlertManager(models.Model):
    phone_number = models.ForeignKey(PhoneNumbers, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    location = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    # alert_started = models.DateTimeField(null=True, blank=True)
    # alert_stopped = models.DateTimeField(null=True, blank=True)
    notified = models.BooleanField(default=False)

    class Meta:
        unique_together = ('phone_number', 'timestamp',)

    # def save(self, *args, **kwargs):
    #     if self.latitude is not None and self.longitude is not None:
    #         g = geocoder.mapbox([self.latitude, self.longitude], method='reverse', key=settings.MAPBOX_API_KEY)
    #         if g.ok:
    #             self.location = g.address
    #     super(AlertManager, self).save(*args, **kwargs)
