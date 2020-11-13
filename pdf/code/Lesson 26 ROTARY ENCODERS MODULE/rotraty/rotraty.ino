/******************************************
 *Website: www.elegoo.com
 * 
 *Time:2017.12.12
 *
 ******************************************/
//Define the pin connection
int CLK = 2;//CLK->D2
int DT = 3;//DT->D3
int SW = 4;//SW->D4
const int interrupt0 = 0;// Interrupt 0 在 pin 2 上
int count = 0;//Define the count
int lastCLK = 0;//CLK initial value
 
void setup()
{
  pinMode(SW, INPUT);
  digitalWrite(SW, HIGH);
  pinMode(CLK, INPUT);
  pinMode(DT, INPUT);
  attachInterrupt(interrupt0, ClockChanged, CHANGE);//Set the interrupt 0 handler, trigger level change

  Serial.begin(9600);
}
 
void loop()
{
  if (!digitalRead(SW) && count != 0) //Read the button press and the count value to 0 when the counter reset

  {
    count = 0;
    Serial.print("count:");
    Serial.println(count);
  }
}
 
//The interrupt handlers
void ClockChanged()
{
  int clkValue = digitalRead(CLK);//Read the CLK pin level
  int dtValue = digitalRead(DT);//Read the DT pin level
  if (lastCLK != clkValue)
  {
    lastCLK = clkValue;
    count += (clkValue != dtValue ? 1 : -1);//CLK and inconsistent DT + 1, otherwise - 1

    Serial.print("count:");
    Serial.println(count);
  }
}
