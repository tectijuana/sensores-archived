/*
 * Author: SMRAZA KEEN
 * Date:2016/6/29
 * IDE V1.6.9
 * Email:TechnicSmraza@outlook.com
 * Function:
 */
#include <LiquidCrystal.h>
#include <dht11.h>                  
dht11 DHT;                  //Note:DHT on behalf of the temperature and humidity sensor 
const int dht11_data = 6;     
int temp=0;
int hum=0;
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup()                                                                                     
{
  lcd.begin(16,2);
  lcd.print("  Welcome to ");
  lcd.setCursor(0,1);
  lcd.print("     Smraza");
  delay(2000);
  lcd.clear();
}
void loop()
{ 
  DHT.read(dht11_data);
  temp=DHT.temperature;
  hum=DHT.humidity;
  lcd.clear();                   //clear display
  lcd.print("Hum=%");            //display "Hum=%"
  lcd.print(hum);
  lcd.setCursor(10,0) ;
  lcd.print("Smraza");           //display "Smraza"
  lcd.setCursor(0,1) ;           //Display position
  lcd.print("Temp=");            //display"Temp="
  lcd.print(temp);
  lcd.write(0xDF);              //Display custom characters '°'
  lcd.print("C");
  delay(500);                   //After 500ms ,the screen will be refreshed
}

