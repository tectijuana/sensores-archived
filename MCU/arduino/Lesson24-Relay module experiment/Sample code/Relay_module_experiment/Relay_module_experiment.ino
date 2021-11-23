/*
 * Author: SMRAZA KEEN
 * Date:2016/6/29
 * IDE V1.6.9
 * Email:TechnicSmraza@outlook.com
 * Function:
 */
const int buttonPin = 2;  
const int relay = 8;      

int relayState = HIGH;         //Relay state
int buttonState;             //Key state
int lastButtonState = LOW;   //Last time the key data

long lastDebounceTime = 0;  // Last output pin trigger time
long debounceDelay = 50;    //Elimination of jitter, if the output is not stable increase in time

void setup() {
  pinMode(buttonPin, INPUT);
  pinMode(relay, OUTPUT);
  digitalWrite(relay, relayState);
}

void loop() {
  int reading = digitalRead(buttonPin); //Read button data

  if (reading != lastButtonState) {
    lastDebounceTime = millis();
  }

  if ((millis() - lastDebounceTime) > debounceDelay){
    if (reading != buttonState) {
      buttonState = reading;

      if (buttonState == HIGH) {
        relayState = !relayState;
      }
    }
  }
  digitalWrite(relay, relayState);
  lastButtonState = reading;
}

