from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Student, EmergencyAlert, AdministratorUser, Device, Location
from .serializers import (
    StudentSerializer,
    EmergencyAlertSerializer,
    AdministratorUserSerializer,
    DeviceSerializer,
    LocationSerializer,
)
@csrf_exempt
def emergency_alert(request, id=""):
    if request.method == 'GET':
        alerts = EmergencyAlert.objects.all()
        alerts_serializer = EmergencyAlertSerializer(alerts, many=True)
        return JsonResponse(alerts_serializer.data, safe=False)

    elif request.method == 'POST':
        alert_data = JSONParser().parse(request)
        alerts_serializer = EmergencyAlertSerializer(data=alert_data)
        if alerts_serializer.is_valid():
            alerts_serializer.save()
            return JsonResponse({"message": "Added Successfully"}, status=201)
        return JsonResponse(alerts_serializer.errors, status=400)

    elif request.method == 'PUT':
        alert_data = JSONParser().parse(request)
        try:
            alert = EmergencyAlert.objects.get(phoneNumber=alert_data['phoneNumber'])
        except EmergencyAlert.DoesNotExist:
            return JsonResponse({"error": "Emergency Alert not found"}, status=404)

        alerts_serializer = EmergencyAlertSerializer(alert, data=alert_data)
        if alerts_serializer.is_valid():
            alerts_serializer.save()
            return JsonResponse({"message": "Updated Successfully"})
        return JsonResponse(alerts_serializer.errors, status=400)

    elif request.method == 'DELETE':
        try:
            alert = EmergencyAlert.objects.get(phoneNumber=id)
        except EmergencyAlert.DoesNotExist:
            return JsonResponse({"error": "Emergency Alert not found"}, status=404)

        alert.delete()
        return JsonResponse({"message": "Deleted Successfully"})

@csrf_exempt
def Student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        students_serializer = StudentSerializer(students, many=True)
        return JsonResponse(students_serializer.data, safe=False)

    elif request.method == 'POST':
        student_data = JSONParser().parse(request)
        students_serializer = StudentSerializer(data=student_data)
        if students_serializer.is_valid():
            students_serializer.save()
            return JsonResponse({"message": "Added Successfully"}, status=201)
        return JsonResponse(students_serializer.errors, status=400)

    elif request.method == 'PUT':
        student_data = JSONParser().parse(request)
        try:
            student = Student.objects.get(studentId=student_data['studentId'])
        except Student.DoesNotExist:
            return JsonResponse({"error": "Student not found"}, status=404)

        students_serializer = StudentSerializer(student, data=student_data)
        if students_serializer.is_valid():
            students_serializer.save()
            return JsonResponse({"message": "Updated Successfully"})
        return JsonResponse(students_serializer.errors, status=400)

    elif request.method == 'DELETE':
        try:
            student_data = JSONParser().parse(request)
            student = Student.objects.get(studentId=student_data['studentId'])
        except Student.DoesNotExist:
            return JsonResponse({"error": "Student not found"}, status=404)

        student.delete()
        return JsonResponse({"message": "Deleted Successfully"})
@csrf_exempt
def administrator_user(request):
    if request.method == 'GET':
        users = AdministratorUser.objects.all()
        users_serializer = AdministratorUserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)

    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        users_serializer = AdministratorUserSerializer(data=user_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse({"message": "Added Successfully"}, status=201)
        return JsonResponse(users_serializer.errors, status=400)

    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        try:
            user = AdministratorUser.objects.get(employee_id=user_data['employee_id'])
        except AdministratorUser.DoesNotExist:
            return JsonResponse({"error": "Administrator User not found"}, status=404)

        users_serializer = AdministratorUserSerializer(user, data=user_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse({"message": "Updated Successfully"})
        return JsonResponse(users_serializer.errors, status=400)

    elif request.method == 'DELETE':
        try:
            user_data = JSONParser().parse(request)
            user = AdministratorUser.objects.get(employee_id=user_data['employee_id'])
        except AdministratorUser.DoesNotExist:
            return JsonResponse({"error": "Administrator User not found"}, status=404)

        user.delete()
        return JsonResponse({"message": "Deleted Successfully"})

# Device Views
@csrf_exempt
def device_list(request):
    if request.method == 'GET':
        devices = Device.objects.all()
        devices_serializer = DeviceSerializer(devices, many=True)
        return JsonResponse(devices_serializer.data, safe=False)

    elif request.method == 'POST':
        device_data = JSONParser().parse(request)
        devices_serializer = DeviceSerializer(data=device_data)
        if devices_serializer.is_valid():
            devices_serializer.save()
            return JsonResponse({"message": "Added Successfully"}, status=201)
        return JsonResponse(devices_serializer.errors, status=400)

    elif request.method == 'PUT':
        device_data = JSONParser().parse(request)
        try:
            device = Device.objects.get(phone_number=device_data['phone_number'])
        except Device.DoesNotExist:
            return JsonResponse({"error": "Device not found"}, status=404)

        devices_serializer = DeviceSerializer(device, data=device_data)
        if devices_serializer.is_valid():
            devices_serializer.save()
            return JsonResponse({"message": "Updated Successfully"})
        return JsonResponse(devices_serializer.errors, status=400)

    elif request.method == 'DELETE':
        try:
            device_data = JSONParser().parse(request)
            device = Device.objects.get(phone_number=device_data['phone_number'])
        except Device.DoesNotExist:
            return JsonResponse({"error": "Device not found"}, status=404)

        device.delete()
        return JsonResponse({"message": "Deleted Successfully"})

# Location Views
@csrf_exempt
def location_list(request):
    if request.method == 'GET':
        locations = Location.objects.all()
        locations_serializer = LocationSerializer(locations, many=True)
        return JsonResponse(locations_serializer.data, safe=False)

    elif request.method == 'POST':
        location_data = JSONParser().parse(request)
        locations_serializer = LocationSerializer(data=location_data)
        if locations_serializer.is_valid():
            locations_serializer.save()
            return JsonResponse({"message": "Added Successfully"}, status=201)
        return JsonResponse(locations_serializer.errors, status=400)

    elif request.method == 'PUT':
        location_data = JSONParser().parse(request)
        try:
            location = Location.objects.get(location_id=location_data['location_id'])
        except Location.DoesNotExist:
            return JsonResponse({"error": "Location not found"}, status=404)

        locations_serializer = LocationSerializer(location, data=location_data)
        if locations_serializer.is_valid():
            locations_serializer.save()
            return JsonResponse({"message": "Updated Successfully"})
        return JsonResponse(locations_serializer.errors, status=400)

    elif request.method == 'DELETE':
        try:
            location_data = JSONParser().parse(request)
            location = Location.objects.get(location_id=location_data['location_id'])
        except Location.DoesNotExist:
            return JsonResponse({"error": "Location not found"}, status=404)

        location.delete()
        return JsonResponse({"message": "Deleted Successfully"})