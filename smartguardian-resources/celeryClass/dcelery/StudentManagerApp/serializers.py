from rest_framework import serializers
from .models import Student
from DeviceApp.serializers import PhoneNumbersSerializer
from DeviceApp.models import PhoneNumbers

# class StudentSerializer(serializers.ModelSerializer):
#     phone_number = PhoneNumbersSerializer()  # use the PhoneNumbers
#     class Meta:
#         model = Student
#         fields = '__all__' 
#         # fields = ['student_id', 'phone_number', 'primary_location', 'first_name', 'last_name', 'gender']

class StudentSerializer(serializers.ModelSerializer):
    phone_number =  PhoneNumbersSerializer()

    class Meta:
        model = Student
        fields = ['student_id', 'phone_number', 'primary_location', 'first_name', 'last_name', 'gender']

    def create(self, validated_data):
        phone_number_data = validated_data.pop('phone_number')
        phone_number = PhoneNumbers.objects.create(**phone_number_data)
        student = Student.objects.create(phone_number=phone_number, **validated_data)
        return student