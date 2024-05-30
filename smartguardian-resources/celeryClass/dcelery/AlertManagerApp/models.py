from django.db import models
from DeviceApp.models import PhoneNumbers
# Create your models here.
class AlertManager(models.Model):
    phone_number = models.ForeignKey(PhoneNumbers, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    timestamp = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('phone_number', 'timestamp',)