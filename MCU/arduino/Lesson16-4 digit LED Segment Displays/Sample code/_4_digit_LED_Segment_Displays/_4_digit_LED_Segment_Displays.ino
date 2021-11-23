/*
 * Author: SMRAZA KEEN
 * Date:2016/6/29
 * IDE V1.6.9
 * Email:TechnicSmraza@outlook.com
 * Function:
 */
int ASeg = 9;
int BSeg = 13;
int CSeg = 4;
int DSeg = 6;
int ESeg = 7;
int FSeg = 10;
int GSeg = 3;

int a1 = 8;
int a2 = 11;
int a3 = 12;
int a4 = 2;
// set variable
long n = 0;
int x = 100;

int del = 54; // fine adjustment for clock

void setup()
{
  pinMode(a1, OUTPUT);
  pinMode(a2, OUTPUT);
  pinMode(a3, OUTPUT);
  pinMode(a4, OUTPUT);
  pinMode(ASeg, OUTPUT);
  pinMode(BSeg, OUTPUT);
  pinMode(CSeg, OUTPUT);
  pinMode(DSeg, OUTPUT);
  pinMode(ESeg, OUTPUT);
  pinMode(FSeg, OUTPUT);
  pinMode(GSeg, OUTPUT);
}

void loop()
{
   clearLEDS();  // Eliminating ghost
   pickDigit(1);  // Display position 1
   pickNumber((n/x/1000)%10); // Display number
   delayMicroseconds(del);  // Time adjustment
   
   clearLEDS();
   pickDigit(2);
   pickNumber((n/x/100)%10);
   delayMicroseconds(del);
     
   clearLEDS();
   pickDigit(3);
   pickNumber((n/x/10)%10);
   delayMicroseconds(del);
     
   clearLEDS();
   pickDigit(4);
   pickNumber(n/x%10);
     delayMicroseconds(del); 
     n++;    
  }
// Select display position
void pickDigit(int x) 
{
  digitalWrite(a1, LOW);
  digitalWrite(a2, LOW);
  digitalWrite(a3, LOW);
  digitalWrite(a4, LOW);

  switch(x)
  {
  case 1:
    digitalWrite(a1, HIGH);
    break;
  case 2:
    digitalWrite(a2, HIGH);
    break;
  case 3:
    digitalWrite(a3, HIGH);
    break;
  case 4:
    digitalWrite(a4, HIGH);
    break;  
  }
}
// select display number 
void pickNumber(int x) 
 {
   switch(x) {
    
   case 1: one(); break;
   case 2: two(); break;
   case 3: three(); break;
   case 4: four(); break;
   case 5: five(); break;
   case 6: six(); break;
   case 7: seven(); break;
   case 8: eight(); break;
   case 9: nine(); break;
   default: zero(); break;
 }
}

void clearLEDS()  // clear the screen
{
   digitalWrite(ASeg, HIGH);
   digitalWrite(BSeg, HIGH);
   digitalWrite(CSeg, HIGH);
   digitalWrite(DSeg, HIGH);
   digitalWrite(ESeg, HIGH);
   digitalWrite(FSeg, HIGH);
   digitalWrite(GSeg, HIGH);
}

//Display function ‘0-9’
void zero() {
  digitalWrite(ASeg, LOW);
  digitalWrite(BSeg, LOW);
  digitalWrite(CSeg, LOW);
  digitalWrite(DSeg, LOW);
  digitalWrite(ESeg, LOW);
  digitalWrite(FSeg, LOW);
  digitalWrite(GSeg, HIGH);
}

void one() { 
  digitalWrite(ASeg, HIGH);
  digitalWrite(BSeg, LOW);
  digitalWrite(CSeg, LOW);
  digitalWrite(DSeg, HIGH);
  digitalWrite(ESeg, HIGH);
  digitalWrite(FSeg, HIGH);
  digitalWrite(GSeg, HIGH);
}

void two() {
  digitalWrite(ASeg, LOW);
  digitalWrite(BSeg, LOW);
  digitalWrite(CSeg, HIGH);
  digitalWrite(DSeg, LOW);
  digitalWrite(ESeg, LOW);
  digitalWrite(FSeg, HIGH);
  digitalWrite(GSeg, LOW);
}

void three() {
  digitalWrite(ASeg, LOW);
  digitalWrite(BSeg, LOW);
  digitalWrite(CSeg, LOW);
  digitalWrite(DSeg, LOW);
  digitalWrite(ESeg, HIGH);
  digitalWrite(FSeg, HIGH);
  digitalWrite(GSeg, LOW);
}
void four() {
  digitalWrite(ASeg, HIGH);
  digitalWrite(BSeg, LOW);
  digitalWrite(CSeg, LOW);
  digitalWrite(DSeg, HIGH);
  digitalWrite(ESeg, HIGH);
  digitalWrite(FSeg, LOW);
  digitalWrite(GSeg, LOW);
}
void five() {
  digitalWrite(ASeg, LOW);
  digitalWrite(BSeg, HIGH);
  digitalWrite(CSeg, LOW);
  digitalWrite(DSeg, LOW);
  digitalWrite(ESeg, HIGH);
  digitalWrite(FSeg, LOW);
  digitalWrite(GSeg, LOW);
}
void six() {
  digitalWrite(ASeg, LOW);
  digitalWrite(BSeg, HIGH);
  digitalWrite(CSeg, LOW);
  digitalWrite(DSeg, LOW);
  digitalWrite(ESeg, LOW);
  digitalWrite(FSeg, LOW);
  digitalWrite(GSeg, LOW);
}

void seven() {
  digitalWrite(ASeg, LOW);
  digitalWrite(BSeg, LOW);
  digitalWrite(CSeg, LOW);
  digitalWrite(DSeg, HIGH);
  digitalWrite(ESeg, HIGH);
  digitalWrite(FSeg, HIGH);
  digitalWrite(GSeg, HIGH);
}

void eight() {
  digitalWrite(ASeg, LOW);
  digitalWrite(BSeg, LOW);
  digitalWrite(CSeg, LOW);
  digitalWrite(DSeg, LOW);
  digitalWrite(ESeg, LOW);
  digitalWrite(FSeg, LOW);
  digitalWrite(GSeg, LOW);
}

void nine() {
  digitalWrite(ASeg, LOW);
  digitalWrite(BSeg, LOW);
  digitalWrite(CSeg, LOW);
  digitalWrite(DSeg, LOW);
  digitalWrite(ESeg, HIGH);
  digitalWrite(FSeg, LOW);
  digitalWrite(GSeg, LOW);
}
