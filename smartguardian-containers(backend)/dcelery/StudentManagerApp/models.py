from django.db import models
from DeviceApp.models import PhoneNumbers

class Student(models.Model):
    """
    Represents a student in the system.

    Attributes:
        student_id (str): The unique identifier for the student.
        phone_number (PhoneNumbers): The phone number associated with the student.
        primary_location (str): The primary location of the student.
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        gender (str): The gender of the student.
    """

    student_id = models.CharField(max_length=50, primary_key=True)
    phone_number = models.OneToOneField(PhoneNumbers, on_delete=models.CASCADE)
    primary_location = models.CharField(max_length=255, default='')
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='')

    def __str__(self):
        """
        Returns a string representation of the student.

        Returns:
            str: The string representation of the student.
        """
        return f"Student: {self.student_id} - {self.first_name} {self.last_name}"
