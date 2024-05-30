from django.db import models

# Create your models here.
from django.db import models
from DeviceApp.models import PhoneNumbers

class Student(models.Model):
    student_id = models.CharField(max_length=50, primary_key=True)
    phone_number = models.OneToOneField(PhoneNumbers, on_delete=models.CASCADE)
    primary_location = models.CharField(max_length=255, default='')
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='')

    def __str__(self):
        return f"Student: {self.student_id} - {self.first_name} {self.last_name}"
