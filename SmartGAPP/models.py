from django.db import models

class EmergencyAlert(models.Model):
    phone_number = models.IntegerField(default=0)
    student_id = models.CharField(max_length=50, blank=False, null=True)
    location = models.CharField(max_length=255, default='')
    attendee = models.CharField(max_length=200, unique=True) 
    time = models.CharField(max_length=50, default='') 

    def __str__(self):
        return f"Emergency Alert: {self.attendee} - {self.time}"

class AdministratorUser(models.Model):
    employee_id = models.CharField(max_length=50, primary_key=True)
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    password = models.CharField(max_length=255, default='')
    photo = models.ImageField(upload_to='admin_photos/', default='default.jpg')
    log_out_time = models.DateTimeField(default='1970-01-01 00:00:00')
    address = models.TextField(default='')

    def __str__(self):
        return f"Admin User: {self.employee_id} - {self.first_name} {self.last_name}"

class Student(models.Model):
    student_id = models.CharField(max_length=100, unique=True, blank=False, null=True)  
    primary_location = models.CharField(max_length=255, default='')
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    gender = models.CharField(max_length=100, default='')

    def __str__(self):
        return f"Student: {self.student_id} - {self.first_name} {self.last_name}"

class Device(models.Model):
    phone_number = models.IntegerField(primary_key=True)
    student_id = models.CharField(max_length=50, default='', blank=False, null=True)

    def __str__(self):
        return f"Device: {self.phone_number} - {self.student_id}"

class Location(models.Model):
    location_id = models.CharField(max_length=50, primary_key=True)
    time = models.CharField(max_length=50, default='')
    primary_location = models.CharField(max_length=255, default='')

    def __str__(self):
        return f"Location: {self.location_id} - {self.primary_location}"
