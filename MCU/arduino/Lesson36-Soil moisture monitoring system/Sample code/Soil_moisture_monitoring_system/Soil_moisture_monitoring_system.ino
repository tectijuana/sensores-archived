 /*
 * Author: SMRAZA KEEN
 * Date:2016/6/29
 * IDE V1.6.9
 * Email:TechnicSmraza@outlook.com
 * Function:
 */
#include <LiquidCrystal.h>
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
int hum = A0;
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
  Serial.begin(9600);
}
void loop()
{ 
  val=analogRead(hum);
  count=100-(val-435)/5.9;
  lcd.clear();                 //clear display
  lcd.print("Smraza");
  lcd.setCursor(0, 1) ;       
  lcd.print("Humidity=%");          
  lcd.print(count);
  delay(150);   
}
