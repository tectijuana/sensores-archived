/*
 * Author: SMRAZA KEEN
 * Date:2016/6/29
 * IDE V1.6.9
 * Email:TechnicSmraza@outlook.com
 * Function:
 */
int Redled=8;     // set Red LED as “output”
int Yellowled=7;  // set Yellow LED as “output”
int Greenled=6;   // set Green LED as “output”
int Key1=5;       // initialize pin for Red button
int Key2=4;       // initialize pin for Yellow button
int Key3=3;       // initialize pin for Green button
int KeyRest=2;    // initialize pin for reset button
int Red;
int Yellow;
int Green;
void setup()
{
  pinMode(Redled,OUTPUT);
  pinMode(Yellowled,OUTPUT);
  pinMode(Greenled,OUTPUT);
  pinMode(Key1,INPUT);
  pinMode(Key2,INPUT);
  pinMode(Key3,INPUT);
  pinMode(KeyRest,INPUT);
}
void loop()         // repeatedly read pins for buttons
{
  Red=digitalRead(Key1);
  Yellow=digitalRead(Key2);
  Green=digitalRead(Key3);
  if(Red==HIGH)Red_YES();
  if(Yellow==HIGH)Yellow_YES();
  if(Green==HIGH)Green_YES();
}

void Red_YES()  // execute the code until Red light is on; end cycle when reset button is pressed
{
  while(digitalRead(KeyRest)==0)
  {
  digitalWrite(Redled,HIGH);
  digitalWrite(Greenled,LOW);
  digitalWrite(Yellowled,LOW);
  }
  clear_led();
}
void Yellow_YES()  // execute the code until Yellow light is on; end cycle when reset button is pressed
{
  while(digitalRead(KeyRest)==0)
  {
  digitalWrite(Redled,LOW);
  digitalWrite(Greenled,LOW);
  digitalWrite(Yellowled,HIGH);
  }
  clear_led();
}
void Green_YES()   // execute the code until Green light is on; end cycle when reset button is pressed
{
  while(digitalRead(KeyRest)==0)
  {
  digitalWrite(Redled,LOW);
  digitalWrite(Greenled,HIGH);
  digitalWrite(Yellowled,LOW);
  }
  clear_led();
}
void clear_led()   // all LED off
{
  digitalWrite(Redled,LOW);
  digitalWrite(Greenled,LOW);
  digitalWrite(Yellowled,LOW);
}

