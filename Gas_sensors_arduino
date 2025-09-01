// Define the ADC pins for each gas sensor
const int MQ8_PIN = 36;   // ADC1_0
const int MQ135_PIN = 39; // ADC1_3
const int MQ137_PIN = 34; // ADC1_6
const int MQ136_PIN = 35; // ADC1_7
const int MQ4_PIN = 32;   // ADC1_4

void setup() {
  // Start the Serial communication
  Serial.begin(115200);
  
  // Initialize the ADC pins
  pinMode(MQ8_PIN, INPUT);
  pinMode(MQ135_PIN, INPUT);
  pinMode(MQ137_PIN, INPUT);
  pinMode(MQ136_PIN, INPUT);
  pinMode(MQ4_PIN, INPUT);
}

void loop() {
  // Read the analog values from each gas sensor
  int mq8Value = analogRead(MQ8_PIN);
  int mq135Value = analogRead(MQ135_PIN);
  int mq137Value = analogRead(MQ137_PIN);
  int mq136Value = analogRead(MQ136_PIN);
  int mq4Value = analogRead(MQ4_PIN);
  
  // Print the values to the Serial Monitor
  Serial.print("MQ8: ");
  Serial.print(mq8Value);
  Serial.print(" | MQ135: ");
  Serial.print(mq135Value);
  Serial.print(" | MQ137: ");
  Serial.print(mq137Value);
  Serial.print(" | MQ136: ");
  Serial.print(mq136Value);
  Serial.print(" | MQ4: ");
  Serial.println(mq4Value);
  
  // Wait for a second before the next reading
  delay(1000);
}
