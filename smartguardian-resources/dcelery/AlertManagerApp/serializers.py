from rest_framework import serializers

class AlertManagerSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    student_name = serializers.CharField()
    timestamp = serializers.DateTimeField()
    alert_status = serializers.CharField()
    alert_count = serializers.IntegerField()
    location = serializers.CharField()

    class Meta:
        fields = ['phone_number', 'student_name', 'timestamp', 'alert_status', 'alert_count', 'location']



# from rest_framework import serializers

# class AlertManagerSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     firstName = serializers.CharField(max_length=100)
#     surname = serializers.CharField(max_length=100, allow_blank=True)
#     timeTriggerdAlert = serializers.DateTimeField()
#     counts = serializers.IntegerField()
#     location = serializers.CharField(max_length=255, allow_blank=True, allow_null=True)
#     status = serializers.CharField(max_length=20)

#     class Meta:
#         fields = ['id', 'firstName', 'surname', 'timeTriggerdAlert', 'counts', 'location', 'status']
