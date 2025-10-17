#include <Arduino.h>
#include <WiFi.h>
#include <PubSubClient.h>

const char* ssid = "ssid";
const char* password = "password";
const char* mqtt_server = "192.168.1.1"; //takes ip address for local broker or public broker
const int mqtt_port = 1883;
const char* mqtt_sub = "controls";
const char* mqtt_pub = "localization";

volatile float x = 0.0;
volatile float y = 0.0;
volatile float theta = 0.0;
volatile unsigned long last_millis = 0;

WiFiClient espClient;
PubSubClient mqttClient(espClient);

void reconnect();


void setup() {
    Serial.begin(11520);
    WiFi.begin(ssid, password);
    while (!mqttClient.connected()) {
        delay(250);
    }

    mqttClient.setServer(mqtt_server, mqtt_port);
    //mqttClient.setCallback(user_input); to be continued
}

void loop() {
    if (!mqttClient.connected()) {
        reconnect();
    }
    mqttClient.loop();

    if (millis() - last_millis > 1000 ) {
        last_millis = millis();
        char msg[20];
        sprintf(msg, "%.2f,%.2f,%.2f", x, y, theta);
        mqttClient.publish(mqtt_pub, msg);
    }
}

void reconnect() {
    while (!mqttClient.connected()) {
        if (mqttClient.connect("ESP32Client")) {
            mqttClient.subscribe(mqtt_sub);
        }
    }
}