#define E1 10  // Enable Pin for motor 1
#define E2 11  // Enable Pin for motor 2
 
#define I1 34  // Control pin 1 for motor 1
#define I2 35  // Control pin 2 for motor 1
#define I3 40  // Control pin 1 for motor 2
#define I4 41  // Control pin 2 for motor 2
#define ID 13  // Control pin 2 for motor 2
 
void setup() {
 
    pinMode(E1, OUTPUT);
    pinMode(E2, OUTPUT);
 
    pinMode(I1, OUTPUT);
    pinMode(I2, OUTPUT);
    pinMode(I3, OUTPUT);
    pinMode(I4, OUTPUT);
    pinMode(ID, OUTPUT);

}
 
void loop() {
 
 
 
    digitalWrite(I1, HIGH);
    digitalWrite(I2, LOW);
    digitalWrite(I3, HIGH);
    digitalWrite(I4, LOW);
    digitalWrite(ID, HIGH);
    delay(10000);
 
    // change direction
 
    digitalWrite(I1, LOW);
    digitalWrite(I2, HIGH);
    digitalWrite(I3, LOW);
    digitalWrite(I4, HIGH);
 
    delay(10000);
}
