int relay = 13;
// the setup routine runs once when you press reset: 
void setup() {
 pinMode(relay, OUTPUT);
}
// the loop routine runs over and over again forever: 
void loop() {
digitalWrite(relay, HIGH);    // turn the relay on (HIGH is the voltage level)
delay(1000); // wait for a second
digitalWrite(relay, LOW);   // turn the LED off by making the voltage LOW 
delay(1000);  // wait for a second
}

