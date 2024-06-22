#include <WiFi.h>
#include <WiFiClientSecure.h>
#include <PubSubClient.h>

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

WiFiClientSecure espClient;
PubSubClient mqttClient(espClient);

unsigned long lastReconnectAttempt = 0;
const long reconnectInterval = 5000;
unsigned long lastPublishTime = 0;
const long publishInterval = 5000;

#define MSG_BUFFER_SIZE (50)
char msg[MSG_BUFFER_SIZE];

// Certificate
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

// Pin where the button is connected
const int buttonPin = 4;
// Pin where the vibrating motor is connected
const int motorPin = 2;

// Initial alert state
bool alert = false;

void setup() {
  Serial.begin(115200);

  // Initialize the button pin as an input
  pinMode(buttonPin, INPUT_PULLUP);
  // Initialize the motor pin as an output
  pinMode(motorPin, OUTPUT);

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
}

void loop() {
  // Maintain WiFi and MQTT connection
  maintainWiFiConnection();
  if (!mqttClient.connected()) {
    reconnect();
  }
  mqttClient.loop();

  // Check the button state
  handleButtonPress();

  // Publish coordinates periodically
  if (millis() - lastPublishTime >= publishInterval) {
    publishCoordinates();
    lastPublishTime = millis();
  }
}

void handleButtonPress() {
  // Read the button state
  int buttonState = digitalRead(buttonPin);

  // Check if the button is pressed
  if (buttonState == LOW) {
    // Toggle the alert state
    alert = !alert;

    // Control the motor based on the alert state
    if (alert) {
      digitalWrite(motorPin, HIGH); // Turn on the motor
    } else {
      digitalWrite(motorPin, LOW); // Turn off the motor
    }

    // Publish the coordinates with the updated alert status
    publishCoordinates();

    // Debounce delay
    delay(500);
  }
}

void publishCoordinates() {
  // Dummy GPS coordinates
  float latitude = -15.391750822378; // London
  float longitude = 35.346897102955296;
  String device_id  = "0885413676";

  // Create a JSON string with dummy GPS data and ID
  String payload = "{\"device_id\":\"" + device_id + "\",\"latitude\":" + String(latitude, 6) + ",\"longitude\":" + String(longitude, 6) + ",\"alert\":" + String(alert ? "true" : "false") + "}";

  // Publish the GPS data to MQTT topic
  mqttClient.publish(mqttTopic, payload.c_str());
  Serial.print("GPS data published: ");
  Serial.println(payload);
}

void reconnect() {
  // Check if it's time to attempt a reconnect
  if (millis() - lastReconnectAttempt < reconnectInterval) {
    return;
  }

  // Attempt to reconnect
  Serial.println("Attempting MQTT reconnection...");
  if (mqttClient.connect(mqttClientId, mqttUsername, mqttPassword)) {
    Serial.println("Reconnected to MQTT broker");
    mqttClient.subscribe(mqttTopic); // Resubscribe to the topic to verify messages
  } else {
    Serial.print("Failed to reconnect to MQTT broker, rc=");
    Serial.println(mqttClient.state());
  }

  // Update last reconnect attempt timestamp
  lastReconnectAttempt = millis();
}

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (unsigned int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();
}

void connectToWiFi() {
  WiFi.mode(WIFI_STA);
  Serial.println("Connecting to Wi-Fi...");
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nConnected to Wi-Fi");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
}
void maintainWiFiConnection() {
  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("WiFi connection lost. Reconnecting...");
    connectToWiFi();
  }
}
