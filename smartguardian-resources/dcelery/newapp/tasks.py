# # import threading
# # from celery import shared_task,app
# # import paho.mqtt.client as mqtt
# # import json
# # from DeviceApp.models import LocationManager

# # class MQTTSubscriber:
# #     def __init__(self, broker_address, username, password):
# #         self.broker_address = broker_address
# #         self.username = username
# #         self.password = password
# #         self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
# #         self.client.tls_set()
# #         self.client.username_pw_set(username, password)
# #         self.client.on_connect = self.on_connect
# #         self.client.on_message = self.on_message

# #     def on_connect(self, client, userdata, flags, rc, properties):
# #         print(f'Connected with result code {rc}')
# #         if rc == 0:
# #             client.subscribe("gps/+")  # Subscribe to the topic

# #     def on_message(self, client, userdata, message):
# #         topic = message.topic
# #         payload = str(message.payload.decode("utf-8"))
# #         print("Received message:", payload, "on topic:", topic)
# #         try:
# #             # Load JSON data
# #             data = json.loads(payload)

# #             # Extract fields
# #             device_id = data.get("device_id")
# #             latitude = data.get("latitude")
# #             longitude = data.get("longitude")
# #             alert = data.get("alert")

# #             # Create a new LocationManager object
# #             location = LocationManager(device_id=device_id, latitude=latitude, longitude=longitude, alert=alert)
            
# #             # Save the object to the database
# #             location.save()
            
# #             print("Data written to database successfully.")
# #         except Exception as e:
# #             print(f"Error writing data to database: {e}")
    

        

# # @shared_task
# # def mqtt_subscriber_task():
# #     broker_address = "20d34d0715dc40bd94844427c77b2dd5.s1.eu.hivemq.cloud"
# #     username = "SmartGuardian"
# #     password = "BSC-COM-NE-15-19@unima.ac.mw"

# #     subscriber = MQTTSubscriber(broker_address, username, password)
# #     subscriber.client.connect(subscriber.broker_address, 8883)
# #     subscriber.client.loop_forever()

# # # Start the MQTT subscriber in a separate thread
# # mqtt_thread = threading.Thread(target=mqtt_subscriber_task)
# # mqtt_thread.start()

# import threading
# from celery import shared_task
# import paho.mqtt.client as mqtt
# import json
# from DeviceApp.models import LocationManager

# class MQTTSubscriber:
#     def __init__(self, broker_address, username, password):
#         self.broker_address = broker_address
#         self.username = username
#         self.password = password
#         self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
#         self.client.tls_set()
#         self.client.username_pw_set(username, password)
#         self.client.on_connect = self.on_connect
#         self.client.on_message = self.on_message

#     def on_connect(self, client, userdata, flags, rc, properties):
#         print(f'Connected with result code {rc}')
#         if rc == 0:
#             client.subscribe("gps/+")  # Subscribe to the topic

#     def on_message(self, client, userdata, message):
#         topic = message.topic
#         payload = str(message.payload.decode("utf-8"))
#         print("Received message:", payload, "on topic:", topic)
#         try:
#             # Load JSON data
#             data = json.loads(payload)

#             # Extract fields
#             device_id = data.get("device_id")
#             latitude = data.get("latitude")
#             longitude = data.get("longitude")
#             alert = data.get("alert")

#             # Create a new LocationManager object
#             location = LocationManager(device_id=device_id, latitude=latitude, longitude=longitude, alert=alert)
            
#             # Save the object to the database
#             location.save()
            
#             print("Data written to database successfully.")
#         except Exception as e:
#             print(f"Error writing data to database: {e}")

# @shared_task
# def mqtt_subscriber_task():
#     broker_address = "20d34d0715dc40bd94844427c77b2dd5.s1.eu.hivemq.cloud"
#     username = "SmartGuardian"
#     password = "BSC-COM-NE-15-19@unima.ac.mw"

#     subscriber = MQTTSubscriber(broker_address, username, password)
#     subscriber.client.connect(subscriber.broker_address, 8883)
#     subscriber.client.loop_start()  # Start the MQTT client loop

# # Start the MQTT subscriber in a separate thread
# mqtt_thread = threading.Thread(target=mqtt_subscriber_task)
# mqtt_thread.start()







































# # Define a Celery task
# # @app.task
# # def process_data(data):
    
# #     # Process your data here

# #     try:
# #         # Load JSON data
# #         data = json.loads(data)

# #         # Extract fields
# #         device_id = data.get("device_id")
# #         latitude = data.get("latitude")
# #         longitude = data.get("longitude")
# #         alert = data.get("alert")

# #         # Create a new LocationManager object
# #         location = LocationManager(device_id=device_id, latitude=latitude, longitude=longitude, alert=alert)
        
# #         # Save the object to the database
# #         location.save()
        
# #         print("Data written to database successfully.")
# #     except Exception as e:
# #         print(f"Error writing data to database: {e}")
# #     pass





# # tasks.py

# # from celery import Celery
# # from paho.mqtt import client as mqtt_client
# # import json
# # import psycopg2
# # import os
# # from DeviceApp.models import LocationManager


# # # Initialize Celery with broker and result backend URLs from environment variables
# # app = Celery('tasks', broker=os.environ.get("CELERY_BROKER", "redis://redis:6379/0"), backend=os.environ.get("CELERY_BACKEND", "redis://redis:6379/0"))

# # # Database settings
# # db_config = {
# #     'database': os.environ.get("POSTGRES_DB"),
# #     'user': os.environ.get("POSTGRES_USER"),
# #     'password': os.environ.get("POSTGRES_PASSWORD"),
# #     'host': 'postgres',  # Or your database host
# #     'port': '5432',
# # }

# # # MQTT settings
# # broker = '20d34d0715dc40bd94844427c77b2dd5.s1.eu.hivemq.cloud'
# # port = 8883
# # topic = "gps/+"
# # client_id = 'mqtt.CallbackAPIVersion.VERSION2'

# # # MQTT callback function
# # def on_message(client, userdata, msg):
# #     print(f'Received `{msg.payload.decode()}` from `{msg.topic}` topic')
# #     json_data = json.loads(msg.payload.decode())
# #     process_data.delay(json_data)

# # @app.task
# # def process_data(json_data):
# #     # Process your data here

# #     try:
# #         # Load JSON data
# #         data = json.loads(json_data)

# #         # Extract fields
# #         device_id = data.get("device_id")
# #         latitude = data.get("latitude")
# #         longitude = data.get("longitude")
# #         alert = data.get("alert")

# #         # Create a new LocationManager object
# #         location = LocationManager(device_id=device_id, latitude=latitude, longitude=longitude, alert=alert)
        
# #         # Save the object to the database
# #         location.save()
        
# #         print("Data written to database successfully.")
# #     except Exception as e:
# #         print(f"Error writing data to database: {e}")


# #     # Create a new LocationManager object
# #     # location = LocationManager(device_id=data.device_id, latitude=latitude, longitude=longitude, alert=alert)
# #     # # Save the object to the database
# #     # location.save()
# #     # This could involve writing it to a database, checking for alerts, etc.
# #     pass

# # # MQTT setup
# # def run_mqtt():
# #     client = mqtt_client.Client(client_id)
# #     client.on_message = on_message
# #     client.username_pw_set('SmartGuardian', 'BSC-COM-NE-15-19@unima.ac.mw')  # MQTT username and password
# #     client.tls_set()
# #     client.connect(broker, port)
# #     client.subscribe(topic)
# #     client.loop_start()

# # # Run MQTT in a separate thread
# # import threading
# # threading.Thread(target=run_mqtt).start()
