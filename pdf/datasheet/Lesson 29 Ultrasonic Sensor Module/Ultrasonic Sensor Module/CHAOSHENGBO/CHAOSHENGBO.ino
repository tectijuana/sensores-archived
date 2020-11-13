
#define TRIGGER 12
#define ECHO 11

void setup()
{
pinMode(ECHO, INPUT);
pinMode(TRIGGER, OUTPUT);
digitalWrite(TRIGGER, LOW);
Serial.begin(9600);
}
void loop()
{
long distance, duration;
digitalWrite(TRIGGER, HIGH);
delayMicroseconds(10);
digitalWrite(TRIGGER, LOW);
duration = pulseIn(ECHO,HIGH);
distance = duration / 2 / 7.6;
Serial.println(distance);
}
