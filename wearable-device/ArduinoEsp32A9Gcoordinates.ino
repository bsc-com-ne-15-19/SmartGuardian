#include <WiFi.h>
#include <WiFiClientSecure.h>
#include <PubSubClient.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

// Replace the next variables with your Wi-Fi credentials
const char* ssid = "802.11.1";
const char* password = "12345689";

// Add your MQTT Broker IP address and port
const char* mqttBroker = "20d34d0715dc40bd94844427c77b2dd5.s1.eu.hivemq.cloud";
const int mqttPort = 8883;

const char* mqttClientId = "mqtt.Client"; // Change to a unique string
const char* mqttUsername = "SmartGuardian";
const char* mqttPassword = "BSC-COM-NE-15-19@unima.ac.mw";
const char* mqttTopic = "gps/0995257479";

// Certificate for SSL/TLS connection (if required)
static const char* root_ca PROGMEM = R"EOF(
-----BEGIN CERTIFICATE-----
MIIFazCCA1OgAwIBAgIRAIIQz7DSQONZRGPgu2OCiwAwDQYJKoZIhvcNAQELBQAw
TzELMAkGA1UEBhMCVVMxKTAnBgNVBAoTIEludGVybmV0IFNlY3VyaXR5IFJlc2Vh
cmNoIEdyb3VwMRUwEwYDVQQDEwxJU1JHIFJvb3QgWDEwHhcNMTUwNjA0MTEwNDM4
WhcNMzUwNjA0MTEwNDM4WjBPMQswCQYDVQQGEwJVUzEpMCcGA1UEChMgSW50ZXJu
ZXQgU2VjdXJpdHkgUmVzZWFyY2ggR3JvdXAxFTATBgNVBAMTDElTUkcgUm9vdCBY
MTCCAiIwDQYJKoZIhvcNAQEBBQADggIPADCCAgoCggIBAK3oJHP0FDfzm54rVygc
h77ct984kIxuPOZXoHj3dcKi/vVqbvYATyjb3miGbESTtrFj/RQSa78f0uoxmyF+
0TM8ukj13Xnfs7j/EvEhmkvBioZxaUpmZmyPfjxwv60pIgbz5MDmgK7iS4+3mX6U
A5/TR5d8mUgjU+g4rk8Kb4Mu0UlXjIB0ttov0DiNewNwIRt18jA8+o+u3dpjq+sW
T8KOEUt+zwvo/7V3LvSye0rgTBIlDHCNAymg4VMk7BPZ7hm/ELNKjD+Jo2FR3qyH
B5T0Y3HsLuJvW5iB4YlcNHlsdu87kGJ55tukmi8mxdAQ4Q7e2RCOFvu396j3x+UC
B5iPNgiV5+I3lg02dZ77DnKxHZu8A/lJBdiB3QW0KtZB6awBdpUKD9jf1b0SHzUv
KBds0pjBqAlkd25HN7rOrFleaJ1/ctaJxQZBKT5ZPt0m9STJEadao0xAH0ahmbWn
OlFuhjuefXKnEgV4We0+UXgVCwOPjdAvBbI+e0ocS3MFEvzG6uBQE3xDk3SzynTn
jh8BCNAw1FtxNrQHusEwMFxIt4I7mKZ9YIqioymCzLq9gwQbooMDQaHWBfEbwrbw
qHyGO0aoSCqI3Haadr8faqU9GY/rOPNk3sgrDQoo//fb4hVC1CLQJ13hef4Y53CI
rU7m2Ys6xt0nUW7/vGT1M0NPAgMBAAGjQjBAMA4GA1UdDwEB/wQEAwIBBjAPBgNV
HRMBAf8EBTADAQH/MB0GA1UdDgQWBBR5tFnme7bl5AFzgAiIyBpY9umbbjANBgkq
hkiG9w0BAQsFAAOCAgEAVR9YqbyyqFDQDLHYGmkgJykIrGF1XIpu+ILlaS/V9lZL
ubhzEFnTIZd+50xx+7LSYK05qAvqFyFWhfFQDlnrzuBZ6brJFe+GnY+EgPbk6ZGQ
3BebYhtF8GaV0nxvwuo77x/Py9auJ/GpsMiu/X1+mvoiBOv/2X/qkSsisRcOj/KK
NFtY2PwByVS5uCbMiogziUwthDyC3+6WVwW6LLv3xLfHTjuCvjHIInNzktHCgKQ5
ORAzI4JMPJ+GslWYHb4phowim57iaztXOoJwTdwJx4nLCgdNbOhdjsnvzqvHu7Ur
TkXWStAmzOVyyghqpZXjFaH3pO3JLF+l+/+sKAIuvtd7u+Nxe5AW0wdeRlN8NwdC
jNPElpzVmbUq4JUagEiuTDkHzsxHpFKVK7q4+63SM1N95R1NbdWhscdCb+ZAJzVc
oyi3B43njTOQ5yOf+1CceWxG1bQVs5ZufpsMljq4Ui0/1lvh+wjChP4kqKOJ2qxq
4RgqsahDYVvTH9w7jXbyLeiNdd8XM2w9U/t7y0Ff/9yi0GE44Za4rF2LN9d11TPA
mRGunUHBcnWEvgJBQl9nJEiU0Zsnvgc/ubhPgXRR4Xq37Z0j4r7g1SgEEzwxA57d
emyPxgcYxn/eR44/KJ4EBs+lVDR3veyJm+kXQ99b21/+jh5Xos1AnX5iItreGCc=
-----END CERTIFICATE-----
)EOF";

// MQTT and WiFi clients
WiFiClientSecure espClient;
PubSubClient mqttClient(espClient);

unsigned long lastReconnectAttempt = 0;
const long reconnectInterval = 5000;
unsigned long lastPublishTime = 0;
const long publishInterval = 5000;

// Serial communication pins for A9G module
const int RX_PIN = 16;
const int TX_PIN = 17;

// Button and motor pin definitions
const int BUTTON_PIN = 4;
const int MOTOR_PIN = 2;

bool alert = false;

void setup() {
  Serial.begin(115200);
  Serial2.begin(115200, SERIAL_8N1, RX_PIN, TX_PIN); // Initialize serial communication with A9G module

  pinMode(BUTTON_PIN, INPUT);
  pinMode(MOTOR_PIN, OUTPUT);
  digitalWrite(BUTTON_PIN, HIGH); // Enable internal pull-up resistor for the button

  // Connect to Wi-Fi
  connectToWiFi();

  // Set the root certificate for the connection
  espClient.setCACert(root_ca);

  // Connect to MQTT broker
  mqttClient.setServer(mqttBroker, mqttPort);
  mqttClient.setCallback(callback);

  // Wait for MQTT connection
  while (!mqttClient.connected()) {
    Serial.println("Connecting to MQTT broker...");
    if (mqttClient.connect(mqttClientId, mqttUsername, mqttPassword)) {
      Serial.println("Connected to MQTT broker");
      mqttClient.subscribe(mqttTopic); // Subscribe to the topic to verify messages
    } else {
      Serial.print("Failed to connect to MQTT broker, rc=");
      Serial.print(mqttClient.state());
      Serial.println(" Retrying in 5 seconds...");
      delay(5000); // Increase the delay to 5 seconds
    }
  }

  // Enable GPS on the A9G module
  //Serial2.println("AT+GPS=1");
  //delay(1000); // Give the module some time to process the command
  //Serial2.println("AT+GPSRD=2");
}

void loop() {
  // Maintain MQTT connection
  if (!mqttClient.connected()) {
    reconnect();
  }
  mqttClient.loop();

  // Check button state
  checkButton();

  // Publish coordinates periodically
  if (millis() - lastPublishTime >= publishInterval) {
    publishCoordinates();
    lastPublishTime = millis();
  }
}

void checkButton() {
  static bool lastButtonState = false;
  bool buttonState = digitalRead(BUTTON_PIN);
  
  if (buttonState != lastButtonState) {
    delay(50); // debounce delay
    buttonState = digitalRead(BUTTON_PIN); // read again
    
    if (buttonState == LOW) {
      // Button pressed
      alert = !alert;
      if (alert) {
        Serial.println("Alert activated");
        vibrateMotor(); // Activate motor on button press
      } else {
        Serial.println("Alert deactivated");
        stopMotor();
      }

      // Publish state to MQTT
      publishAlertState();
    }
  }
  lastButtonState = buttonState;
}

void publishAlertState() {
  String device_id = "0995257479";
  String alertState = alert ? "true" : "false";

  // Create the JSON payload string with alert state
  String payload = "{\"device_id\":\"" + device_id + "\",\"latitude\":0.0,\"longitude\":0.0,\"alert\":" + alertState + "}";

  // Publish the GPS data to MQTT topic
  mqttClient.publish(mqttTopic, payload.c_str());
  Serial.print("Alert state published: ");
  Serial.println(payload);
}

void publishCoordinates() {
  if (Serial2.available()) {
    String gpsData = Serial2.readStringUntil('\n');
    Serial.println("GPS Data: " + gpsData);

    if (gpsData.startsWith("+GPSRD:")) {
      float latitude = parseLatitude(gpsData);
      float longitude = parseLongitude(gpsData);

      String device_id = "0995257479";

      // Create the JSON payload string with alert state
      String alertState = alert ? "true" : "false";
      String payload = "{\"device_id\":\"" + device_id + "\",\"latitude\":" + String(latitude, 6) + ",\"longitude\":" + String(longitude, 6) + ",\"alert\":" + alertState + "}";

      // Publish the GPS data to MQTT topic
      mqttClient.publish(mqttTopic, payload.c_str());
      Serial.print("GPS data published: ");
      Serial.println(payload);
    }
  }
}

float parseLatitude(String gpsData) {
  // Example: +GPSRD: $GPGGA,123456.00,3723.2475,N,12202.3242,W,1,10,0.78,9.0,M,-25.669,M,,*76
  int latStart = gpsData.indexOf(",") + 1;
  latStart = gpsData.indexOf(",", latStart) + 1;
  int latEnd = gpsData.indexOf(",", latStart);
  String latString = gpsData.substring(latStart, latEnd);
  return convertToDecimal(latString.toFloat(), gpsData.charAt(latEnd + 1));
}

float parseLongitude(String gpsData) {
  int lonStart = gpsData.indexOf(",", gpsData.indexOf(",") + 1) + 1;
  lonStart = gpsData.indexOf(",", lonStart) + 1;
  lonStart = gpsData.indexOf(",", lonStart) + 1;
  int lonEnd = gpsData.indexOf(",", lonStart);
  String lonString = gpsData.substring(lonStart, lonEnd);
  return convertToDecimal(lonString.toFloat(), gpsData.charAt(lonEnd + 1));
}

float convertToDecimal(float coord, char direction) {
  int degrees = (int)(coord / 100);
  float minutes = coord - (degrees * 100);
  float decimal = degrees + (minutes / 60.0);
  if (direction == 'S' || direction == 'W') {
    decimal *= -1;
  }
  return decimal;
}

void callback(char* topic, byte* message, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)message[i]);
  }
  Serial.println();
}

void reconnect() {
  if (WiFi.status() != WL_CONNECTED) {
    connectToWiFi();
  }
  Serial.println("Attempting MQTT reconnection...");
  // Attempt to reconnect
  if (mqttClient.connect(mqttClientId, mqttUsername, mqttPassword)) {
    Serial.println("Reconnected to MQTT broker");
    mqttClient.subscribe(mqttTopic);
  } else {
    Serial.print("Failed to reconnect to MQTT broker, rc=");
    Serial.print(mqttClient.state());
    Serial.println(" Retrying in 5 seconds...");
  }
}

void connectToWiFi() {
  Serial.println("Connecting to Wi-Fi...");
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to Wi-Fi");
}

void maintainWiFiConnection() {
  if (WiFi.status() != WL_CONNECTED) {
    connectToWiFi();
  }
}

void vibrateMotor() {
  digitalWrite(MOTOR_PIN, HIGH); // Activate the motor
}

void stopMotor() {
  digitalWrite(MOTOR_PIN, LOW); // Deactivate the motor
}
