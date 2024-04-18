from django.contrib import admin

# Register your models here.

from .models import EmergencyAlert, AdministratorUser, Device, Location, Student

admin.site.register(EmergencyAlert)
admin.site.register(AdministratorUser)
admin.site.register(Device)
admin.site.register(Location)
admin.site.register(Student)