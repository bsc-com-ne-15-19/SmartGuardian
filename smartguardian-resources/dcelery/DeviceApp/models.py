
# Create your models here.
from django.db import models

# class LocationManager(models.Model):
#     device_id = models.CharField(max_length=50)
#     latitude = models.DecimalField(max_digits=9, decimal_places=6)
#     longitude = models.DecimalField(max_digits=9, decimal_places=6)
#     alert = models.BooleanField(default=False)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Device ID: {self.device_id}, Latitude: {self.latitude}, Longitude: {self.longitude}, Alert: {self.alert}, Timestamp: {self.timestamp}"

class PhoneNumbers(models.Model):
    phone_number = models.CharField(max_length=30, primary_key=True)
    email_address = models.CharField(max_length=255)
    # location = models.CharField(max_length=100)

class LocationData(models.Model):
    phone_number = models.ForeignKey(PhoneNumbers, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    timestamp = models.DateTimeField(auto_now_add=True)
    student_name = models.CharField(max_length=200, default='')
    alert = models.CharField(max_length=9, default='')
    
    class Meta:
        unique_together = ('phone_number', 'timestamp',)
