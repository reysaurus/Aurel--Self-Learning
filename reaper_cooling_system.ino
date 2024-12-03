#include <DHT.h>

// Pin sensor dan relay
#define DHTPIN 2         // Pin untuk DHT22
#define DHTTYPE DHT22    // Jenis sensor suhu
#define RELAY1_PIN 7     // Pin relay untuk kipas 1
#define RELAY2_PIN 8     // Pin relay untuk kipas 2
#define RELAY3_PIN 9     // Pin relay untuk kipas 3

DHT dht(DHTPIN, DHTTYPE);

// Ambang suhu untuk menyalakan kipas (dalam derajat Celsius)
float thresholdTemp = 30.0;

void setup() {
  Serial.begin(9600);
  dht.begin();
  
  // Menyiapkan pin relay sebagai output
  pinMode(RELAY1_PIN, OUTPUT);
  pinMode(RELAY2_PIN, OUTPUT);
  pinMode(RELAY3_PIN, OUTPUT);

  // Memastikan kipas mati saat robot pertama kali dinyalakan
  digitalWrite(RELAY1_PIN, LOW);
  digitalWrite(RELAY2_PIN, LOW);
  digitalWrite(RELAY3_PIN, LOW);
}

void loop() {
  // Membaca suhu dari DHT22
  float temp = dht.readTemperature();
  
  // Memeriksa apakah pembacaan suhu valid
  if (isnan(temp)) {
    Serial.println("Failed to read temperature");
    return;
  }

  Serial.print("Temperature: ");
  Serial.println(temp);

  // Mengaktifkan kipas jika suhu lebih tinggi dari ambang batas
  if (temp > thresholdTemp) {
    digitalWrite(RELAY1_PIN, HIGH);  // Kipas 1 menyala
    digitalWrite(RELAY2_PIN, HIGH);  // Kipas 2 menyala
    digitalWrite(RELAY3_PIN, HIGH);  // Kipas 3 menyala
  } else {
    digitalWrite(RELAY1_PIN, LOW);   // Kipas 1 mati
    digitalWrite(RELAY2_PIN, LOW);   // Kipas 2 mati
    digitalWrite(RELAY3_PIN, LOW);   // Kipas 3 mati
  }

  delay(2000); // Tunggu 2 detik sebelum membaca suhu lagi
}
