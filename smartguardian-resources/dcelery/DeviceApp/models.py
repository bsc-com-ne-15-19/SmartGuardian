
from django.db import models

class PhoneNumbers(models.Model):
    """
    Model representing phone numbers and associated email addresses.
    It represents the Wearable Device, to avoid confusion with relationships it was just named PhoneNumbers.
    """
    phone_number = models.CharField(max_length=30, primary_key=True)
    email_address = models.CharField(max_length=255)

class LocationData(models.Model):
    """
    Model representing location data of a phone number.
    """
    phone_number = models.ForeignKey(PhoneNumbers, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    timestamp = models.DateTimeField(auto_now_add=True)
    student_name = models.CharField(max_length=200, default='')
    alert = models.CharField(max_length=9, default='')
    
    class Meta:
        unique_together = ('phone_number', 'timestamp',)
