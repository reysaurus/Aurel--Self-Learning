#include <SPI.h>
#include <Wire.h>


#define SPEAKER_PIN 7
#define MIC_PIN A0

VOID setup() {
    Serial.begin(9600);
    pinMode(SPEAKER_PIN, OUTPUT);
    pinMode(MIC_PIN, INPUT);
}

void loop() {
    if (Serial.available()) {
        char command = Serial.read();
        if (command == 'S') {
            digitalWrite(SPEAKER_PIN, HIGH);
        } else if (command == 'M') {
            digitalwrite(SPEAKER_PIN, LOW);
        }
    }
}
