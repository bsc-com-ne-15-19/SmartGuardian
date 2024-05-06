#include <PubSubClient.h>
#include <Wire.h>
#include <GSM.h>

#define SIM800_RX 2 // RX pin of SIM800L connected to D2 of Arduino
#define SIM800_TX 3 // TX pin of SIM800L connected to D3 of Arduino

const char* mqttBroker = "20d34d0715dc40bd94844427c77b2dd5.s1.eu.hivemq.cloud";
const int mqttPort = 8883;
const char* mqttClientId = "arduino_client";
const char* mqttUsername = "SmartGuardian";
const char* mqttPassword = "BSC-COM-NE-15-19@unima.ac.mw";
const char* mqttTopic = "GPS";

GSM gsmAccess;
GPRS gprs;
GSMClient gsmClient;
PubSubClient mqttClient(gsmClient);

void setup() {
  Serial.begin(9600);
  delay(2000);

  Serial.println("Initializing GSM module...");
  pinMode(SIM800_RX, OUTPUT);
  pinMode(SIM800_TX, INPUT);

  Serial.println("AT");
  delay(1000);

  Serial.println("AT+CMEE=2");
  delay(1000);

  // Set band 3 (1800 MHz) for GSM network in Malawi
  Serial.println("AT+Band=3");
  delay(1000);

  // Set the APN (Access Point Name) for your cellular network in Malawi
  Serial.println("AT+SAPBR=3,1,\"CONTYPE\",\"GPRS\"");
  delay(1000);
  Serial.println("AT+SAPBR=3,1,\"APN\",\"internet\"");
  delay(1000);

  if (!initializeGSM()) {
    Serial.println("Failed to initialize GSM module.");
    while (true) {}
  }

  mqttClient.setServer(mqttBroker, mqttPort);
}

void loop() {
  if (!mqttClient.connected()) {
    reconnect();
  }
  mqttClient.loop();
}

bool initializeGSM() {
  if (gsmAccess.begin() != GSM_READY) {
    return false;
  }
  Serial.println("GSM module initialized successfully.");
  return true;
}

void reconnect() {
  while (!mqttClient.connected()) {
    Serial.print("Attempting MQTT connection...");
    if (mqttClient.connect(mqttClientId, mqttUsername, mqttPassword)) {
      Serial.println("connected");
    } else {
      Serial.print("failed, rc=");
      Serial.print(mqttClient.state());
      Serial.println(" try again in 5 seconds");
      delay(5000);
    }
  }
}
