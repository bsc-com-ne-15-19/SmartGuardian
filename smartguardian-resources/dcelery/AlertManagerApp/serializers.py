# This module contains the serializer class for the AlertManager model.
# The AlertManagerSerializer class defines the serialization behavior for the AlertManager model,

from rest_framework import serializers
from .models import AlertManager
from datetime import datetime
from dateutil import parser

class AlertManagerSerializer(serializers.Serializer):
    """
    Serializer class for the AlertManager model.
    """

    phone_number = serializers.CharField()
    student_name = serializers.CharField()
    timestamp = serializers.DateTimeField()
    alert_status = serializers.CharField()
    alert_count = serializers.IntegerField()
    location = serializers.CharField()

    class Meta:
        fields = ['phone_number', 'student_name', 'timestamp', 'alert_status', 'alert_count', 'location']

    def to_representation(self, instance):
        """
        Custom representation method to format the timestamp field.
        """
        ret = super().to_representation(instance)
        ret['timestamp'] = self.format_timestamp(ret['timestamp'])
        return ret

    def format_timestamp(self, timestamp):
        """
        Formats the given timestamp into a human-readable format.

        Args:
            timestamp (str): The timestamp to format.

        Returns:
            str: The formatted timestamp.
        """
        now = datetime.now()
        timestamp_date = parser.isoparse(timestamp)  # Use parser to parse the timestamp
        if now.date() == timestamp_date.date():
            return 'Today at ' + timestamp_date.strftime('%I:%M %p')
        return timestamp_date.strftime('%B %d, %Y at %I:%M %p')

