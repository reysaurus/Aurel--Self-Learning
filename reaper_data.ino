#include <DHT.h> //sensor suhu

#define DHTPIN 2
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);

float batteryVoltage = 12,0; // batere 12V
float currentVoltage = 5.0; // 5V yang dibutuhkan arduino

void setup() {
    Serial.begin(9600);
    dht.begin();
}

void loop() {
    float temprature = dht.readTemperature();
    float humidity = dht.readHumidity();

    // Bagian untuk mengirim data ke control panel Reaper 505
    if (isnan(temprature) || isnan(humidity)) {
        Serial.println("Failed to read from DHT sensor!");
        return;
}

// Kirim seluruh data
Serial.print("Temp: ");
Serial.print(temprature);
Serial.print("*C: ");
Serial.print(humidity);
Serial.print("%: ");
Serial.print(batteryVoltage);
Serial.println("V: ");
Serial.print(currentVoltage);

delay(1000);
}
