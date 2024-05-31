from rest_framework import serializers
from .models import PhoneNumbers
class PhoneNumbersSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumbers
        fields = ['phone_number','email_address']