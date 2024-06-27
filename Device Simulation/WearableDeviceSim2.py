import json
import random
import time
import math
import paho.mqtt.client as mqtt

class GPS:
    def __init__(self, center_lat, center_long, radius):
        self.center_lat = center_lat
        self.center_long = center_long
        self.radius = radius
        self.latitude, self.longitude = self.generate_random_gps()

    def generate_random_gps(self):
        r = self.radius/111300
        u = random.uniform(0,1)
        v = random.uniform(0,1)
        w = r * math.sqrt(u)
        t = 2 * math.pi * v
        x = w * math.cos(t)
        y = w * math.sin(t)
        new_lat = x + self.center_lat
        new_long = y + self.center_long
        return new_lat, new_long

    def update(self):
        self.latitude, self.longitude = self.generate_random_gps()

class Device:
    def __init__(self, id):
        self.id = id

class Topic:
    def __init__(self, device_id):
        self.topic = f'gps/{device_id}'

def on_connect(client, userdata, flags, rc, properties):
    print(f'Connected with result code {rc}')

def on_publish(client, userdata, mid, rc, properties):
    print("Message published")

def main():
    device = Device('0992794036')
    gps = GPS(-15.38853, 35.33802, 15000)
    topic = Topic(device.id)

    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_connect = on_connect
    client.on_publish = on_publish

    client.username_pw_set('SmartGuardian', 'BSC-COM-NE-15-19@unima.ac.mw')
    client.tls_set()
    client.connect('20d34d0715dc40bd94844427c77b2dd5.s1.eu.hivemq.cloud', 8883, 60)

    client.loop_start()

    update_counter = 0  # Add a counter for the updates

    while True:
        gps.update()
        update_counter += 1  # Increment the counter each time the GPS is updated

        # If the counter reaches 10, set alert to True and reset the counter
        if update_counter >= 10:
            alert = True
            update_counter = 0
        else:
            alert = False

        payload = json.dumps({
            'device_id': device.id,
            'latitude': gps.latitude,
            'longitude': gps.longitude,
            'alert': alert
        })
        client.publish(topic.topic, payload)
        time.sleep(1)

if __name__ == '__main__':
    main()
