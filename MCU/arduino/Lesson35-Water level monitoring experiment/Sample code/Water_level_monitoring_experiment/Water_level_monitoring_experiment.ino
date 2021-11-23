/*
 * Author: SMRAZA KEEN
 * Date:2016/6/29
 * IDE V1.6.9
 * Email:TechnicSmraza@outlook.com
 * Function:
 */
#include <LiquidCrystal.h>
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
int water = A0;
int val=0;
int count=0;
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
  val=analogRead(water);
  if(val>220)
  count=val/2.2;
  else
  count=0;
  lcd.clear();                 //clear display
  lcd.print("Smraza");
  lcd.setCursor(0, 1) ;       
  lcd.print("Water Level=%");            
  lcd.print(count);
  delay(150);   
}
