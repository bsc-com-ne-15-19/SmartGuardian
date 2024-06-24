from rest_framework import serializers
from .models import PhoneNumbers

class PhoneNumbersSerializer(serializers.ModelSerializer):
    """
    Serializer class for PhoneNumbers model.

    This serializer is used to convert PhoneNumbers model instances into JSON
    representation and vice versa.

    Attributes:
        model (PhoneNumbers): The PhoneNumbers model class.
        fields (list): The list of fields to include in the serialized output.

    """

    class Meta:
        model = PhoneNumbers
        fields = ['phone_number', 'email_address']
