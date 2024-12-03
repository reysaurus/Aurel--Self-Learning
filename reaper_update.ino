void setup() {
  Serial.begin(9600);  // Mengatur komunikasi serial dengan Orange Pi
  pinMode(13, OUTPUT);  // LED sebagai indikator pembaruan
}

void loop() {
  if (Serial.available()) {
    char received = Serial.read();  // Menerima perintah dari Orange Pi
    if (received == 'U') {
      // Menyalakan LED sebagai indikator bahwa pembaruan sedang dilakukan
      digitalWrite(13, HIGH);
      delay(1000);
      digitalWrite(13, LOW);
    }
  }
}
