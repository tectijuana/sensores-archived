/*
 * Author: SMRAZA KEEN
 * Date:2016/6/29
 * IDE V1.6.9
 * Email:TechnicSmraza@outlook.com
 * Function:
 */
// initialize the library with the numbers of the interface pins
#include <LiquidCrystal.h>
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
void setup()                                                                                     
{
// set up the LCD's number of columns and rows:
  lcd.begin(16,2);
// Print a message to the LCD.
  lcd.print("  Welcome to ");
  lcd.setCursor(0,1);  //Display position
  lcd.print("        Smraza");
}
void loop()
{
// Turn off the display:
  lcd.noDisplay();
  delay(500);
  // Turn on the display:
  lcd.display();
  delay(500);
 }

