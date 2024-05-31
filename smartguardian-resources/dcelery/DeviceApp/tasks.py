import threading
from celery import shared_task
import paho.mqtt.client as mqtt
import json
from .models import LocationData, PhoneNumbers
from StudentManagerApp.models import Student
from AlertManagerApp.models import AlertManager
# from channels.layers import get_channel_layer
# from asgiref.sync import async_to_sync
import logging

# Configure logging
logger = logging.getLogger(__name__)

class MQTTSubscriber:
    def __init__(self, broker_address, username, password):
        self.broker_address = broker_address
        self.username = username
        self.password = password
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        self.client.tls_set()
        self.client.username_pw_set(username, password)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def on_connect(self, client, userdata, flags, rc, properties):
        print(f'Connected with result code {rc}')
        if rc == 0:
            client.subscribe("gps/+")  # Subscribe to the topic

    def on_message(self, client, userdata, message):
        topic = message.topic
        payload = str(message.payload.decode("utf-8"))
        print(f"Received message: {payload} on topic: {topic}")
        try:
            data = json.loads(payload)
            device_id = data.get("device_id")
            latitude = data.get("latitude")
            longitude = data.get("longitude")
            alert = data.get("alert")

            phone_number, created = PhoneNumbers.objects.get_or_create(phone_number=device_id)

            # Retrieve the student's name using the phone number
            student = Student.objects.filter(phone_number__phone_number=device_id).first()
            student_name = f"{student.first_name} {student.last_name}" if student else "Unknown"

            # Save location data with student name
            location = LocationData(phone_number=phone_number, latitude=latitude, longitude=longitude, student_name=student_name,alert=alert)
            location.save()

            if alert:
                alert_manager = AlertManager(phone_number=phone_number, student_name=student_name, latitude=latitude, longitude=longitude)
                alert_manager.save()

            print("Data written to database successfully.")
        except Exception as e:
            print(f"Error processing data: {e}")

@shared_task
def mqtt_subscriber_task():
    broker_address = "20d34d0715dc40bd94844427c77b2dd5.s1.eu.hivemq.cloud"
    username = "SmartGuardian"
    password = "BSC-COM-NE-15-19@unima.ac.mw"

    subscriber = MQTTSubscriber(broker_address, username, password)
    subscriber.client.connect(subscriber.broker_address, 8883)
    subscriber.client.loop_start()  # Start the MQTT client loop

# Start the MQTT subscriber in a separate thread
mqtt_thread = threading.Thread(target=mqtt_subscriber_task)
mqtt_thread.start()
