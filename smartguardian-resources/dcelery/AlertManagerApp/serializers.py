# from rest_framework import serializers
# from .models import AlertManager

# class AlertManagerSerializer(serializers.ModelSerializer):
#     alert_count = serializers.IntegerField()
#     alert_status = serializers.SerializerMethodField()
#     phone_number = serializers.CharField(source='phone_number.phone_number')

#     class Meta:
#         model = AlertManager
#         fields = ['phone_number', 'student_name', 'alert_started', 'alert_stopped', 'alert_status', 'alert_count', 'location']

#     def get_alert_status(self, obj):
#         return 'Ongoing' if obj['alert_stopped'] is None else 'Stopped'

from rest_framework import serializers
from .models import AlertManager
from DeviceApp.serializers import PhoneNumbersSerializer

class AlertManagerSerializer(serializers.ModelSerializer):
    phone_number = PhoneNumbersSerializer(read_only=True)
    alert_count = serializers.IntegerField()
    alert_status = serializers.SerializerMethodField()
    timestamp = serializers.DateTimeField()


    class Meta:
        model = AlertManager
        fields = ['phone_number', 'student_name', 'timestamp', 'alert_status', 'alert_count', 'location']

    def get_alert_status(self, obj):
        return 'Ongoing' if obj.alert_count is None else 'Stopped'
