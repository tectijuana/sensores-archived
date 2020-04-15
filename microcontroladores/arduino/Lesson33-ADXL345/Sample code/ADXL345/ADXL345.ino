#include <Wire.h>
#include <LiquidCrystal.h>
#define Register_ID 0  //Configuration Register Address
#define Register_2D 0x2D
#define Register_X0 0x32
#define Register_X1 0x33
#define Register_Y0 0x34
#define Register_Y1 0x35
#define Register_Z0 0x36
#define Register_Z1 0x37

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);//LCD pin

int ADXAddress = 0xA7>>1; //Converted into 7-bit address
int reading = 0;
int val = 0;
int X0,X1,X_out;
int Y0,Y1,Y_out;
int Z1,Z0,Z_out;
double Xg,Yg,Zg;

void setup()
{
  lcd.begin(16, 2); //Initialization LCD
  delay(100);
  Wire.begin(); //Initialization IIC
  delay(100);
  Wire.beginTransmission(ADXAddress);
  Wire.write(Register_2D);
  Wire.write(8);
  Wire.endTransmission();
  lcd.print(" Welcome to ");
  lcd.setCursor(0,1);
  lcd.print("    Smraza");
  delay(2000);
  lcd.clear();
}

void loop()
{
  Wire.beginTransmission(ADXAddress);
  Wire.write(Register_X0);
  Wire.write(Register_X1);
  Wire.endTransmission();
  Wire.requestFrom(ADXAddress,2);
  if(Wire.available()<=2);
  {
    X0 = Wire.read();
    X1 = Wire.read();
    X1 = X1<<8;
    X_out = X0+X1;
  }
  Wire.beginTransmission(ADXAddress);
  Wire.write(Register_Y0);
  Wire.write(Register_Y1);
  Wire.endTransmission();
  Wire.requestFrom(ADXAddress,2);
  if(Wire.available()<=2);
  {
    Y0 = Wire.read();
    Y1 = Wire.read();
    Y1 = Y1<<8;
    Y_out = Y0+Y1;
  }

  Wire.beginTransmission(ADXAddress);
  Wire.write(Register_Z0);
  Wire.write(Register_Z1);
  Wire.endTransmission();
  Wire.requestFrom(ADXAddress,2);
  if(Wire.available()<=2);
  {
    Z0 = Wire.read();
    Z1 = Wire.read();
    Z1 = Z1<<8;
    Z_out = Z0+Z1;
  }

  Xg = X_out/256.00;
  Yg = Y_out/256.00;
  Zg = Z_out/256.00;
  lcd.clear();
  lcd.print("X=");
  lcd.print(Xg);
  lcd.setCursor(8, 0);
  lcd.print("Y=");
  lcd.print(Yg);
  lcd.setCursor(0, 1);
  lcd.print("Z=");
  lcd.print(Zg);
  lcd.setCursor(10, 1);
  lcd.print("Smraza");
  delay(300); //Delay 0.3 seconds, the refresh rate is adjusted here
}
