import json
import math
import random
import time

import paho.mqtt.client as mqtt


class GPS:

    def __init__(self, center_lat, center_long, pace):
        self.latitude = center_lat
        self.longitude = center_long
        self.pace = pace  # Pace in degrees
        self.direction = 0  # Initial direction in radians

    def update(self):
        # Move in a curved path by updating latitude and longitude
        self.direction += 0.01  # Slight change in direction to create a curve
        self.latitude += self.pace * math.cos(self.direction)
        self.longitude += self.pace * math.sin(self.direction)


class Device:

    def __init__(self, id):
        self.id = id


class Topic:

    def __init__(self, device_id):
        self.topic = f'gps/{device_id}'


def on_connect(client, userdata, flags, rc, properties=None):
    print(f'Connected with result code {rc}')


def on_publish(client, userdata, mid, rc, properties=None):
    print("Message published")


def setup_mqtt_client():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_connect = on_connect
    client.on_publish = on_publish

    client.username_pw_set('SmartGuardian', 'BSC-COM-NE-15-19@unima.ac.mw')
    client.tls_set()
    client.connect('20d34d0715dc40bd94844427c77b2dd5.s1.eu.hivemq.cloud', 8883,
                   60)

    return client


def main():
    device = Device('0992794036')
    gps = GPS(-15.38853, 35.33802, 0.00005)  # Reduced pace for smooth movement
    topic = Topic(device.id)

    client = setup_mqtt_client()
    client.loop_start()

    alert_timer = 0

    while True:
        gps.update()
        alert = False
        if alert_timer < 20:
            alert = True

        payload = json.dumps({
            'device_id': device.id,
            'latitude': gps.latitude,
            'longitude': gps.longitude,
            'alert': alert
        })
        client.publish(topic.topic, payload)
        print(f'Published: {payload}')  # Print payload for debugging

        time.sleep(.5)

        alert_timer += 1
        if alert_timer >= 40:
            alert_timer = 0


if __name__ == '__main__':
    main()
