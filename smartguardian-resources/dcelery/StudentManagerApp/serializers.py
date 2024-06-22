# from rest_framework import serializers
# from .models import Student
# from DeviceApp.serializers import PhoneNumbersSerializer
# from DeviceApp.models import PhoneNumbers
# from DeviceApp.models import LocationData

# # class StudentSerializer(serializers.ModelSerializer):
# #     phone_number = PhoneNumbersSerializer()  # use the PhoneNumbers
# #     class Meta:
# #         model = Student
# #         fields = '__all__' 
# #         # fields = ['student_id', 'phone_number', 'primary_location', 'first_name', 'last_name', 'gender']

# class StudentSerializer(serializers.ModelSerializer):
#     phone_number =  PhoneNumbersSerializer()

#     # device_status = LocationData(phone_number=phone_number)
    
#     class Meta:
#         model = Student
#         fields = ['student_id', 'phone_number', 'primary_location', 'first_name', 'last_name', 'gender','device_status']

#     def create(self, validated_data):
#         phone_number_data = validated_data.pop('phone_number')
#         phone_number = PhoneNumbers.objects.create(**phone_number_data)
#         student = Student.objects.create(phone_number=phone_number, **validated_data)
#         return student

from rest_framework import serializers
from .models import Student
from DeviceApp.serializers import PhoneNumbersSerializer
from DeviceApp.models import PhoneNumbers
from DeviceApp.models import LocationData

class StudentSerializer(serializers.ModelSerializer):
    phone_number = PhoneNumbersSerializer()
    device_status = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ['student_id', 'phone_number', 'primary_location', 'first_name', 'last_name', 'gender', 'device_status']

    def get_device_status(self, obj):
        # Check if the phone number has been used in LocationData
        phone_number = obj.phone_number.phone_number
        exists = LocationData.objects.filter(phone_number=phone_number).exists()
        return exists

    def create(self, validated_data):
        phone_number_data = validated_data.pop('phone_number')
        phone_number, created = PhoneNumbers.objects.get_or_create(**phone_number_data)
        student = Student.objects.create(phone_number=phone_number, **validated_data)
        return student
