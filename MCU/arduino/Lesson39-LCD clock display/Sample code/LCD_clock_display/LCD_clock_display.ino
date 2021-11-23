/*
 * Author: SMRAZA KEEN
 * Date:2016/6/29
 * IDE V1.6.9
 * Email:TechnicSmraza@outlook.com
 * Function:
 */
#include <DS3231.h>
#include <Wire.h>
#include <LiquidCrystal.h>
// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

DS3231 Clock;
//initialize variable
boolean Century=false;
boolean h12;
boolean PM;
byte ADay, AHour, AMinute, ASecond, ABits;
boolean ADy, A12h, Apm;
int second,minute,hour,date,month,year,val; 

String comdata ="";
int numdata[7] = {0},mark = 0;

void setup()                                                                                     
{
  Wire.begin();
  Serial.begin(9600);
// set up the LCD's number of columns and rows:
  lcd.begin(16,2);
// Print a message to the LCD.
  lcd.print("  Welcome to ");
  lcd.setCursor(0,1);  //Display position
  lcd.print("        Smraza");
  Serial.println("set_time :");
  Serial.println("year mouth day week hour minute second");
  Serial.println();
  Serial.println("week : 1 -> Sunday; 2 -> Monday; 3 -> Tuesday:  ....7 -> Saturday");
  Serial.println();
  Serial.println("for example :2016-5-20 Tue 0:33:30  ");
  Serial.println("set_time :");
  Serial.println("16 5 20 3 0 33 30");
  Serial.println();
  delay(2000);
  lcd.clear();
}
void loop() 
{  
   Serial_data();
   delay(150);
}
void WriteDS3231()
{
  Clock.setSecond(numdata[6]); 
  Clock.setMinute(numdata[5]); 
  Clock.setHour(numdata[4]);   
  Clock.setDoW(numdata[3]);    
  Clock.setDate(numdata[2]);   
  Clock.setMonth(numdata[1]);  
  Clock.setYear(numdata[0]);   
}
void Serial_data()
{
  int j = 0;
  while (Serial.available() > 0)    //Serial data detection
  {
    comdata += char(Serial.read());
    delay(2);
    mark = 1;
    Print_time();
  }
  if(mark == 1)  
  {
    Serial.println(comdata);             //Already detected data
    for(int i = 0; i < comdata.length() ; i++) //data conversion
    {
      if(comdata[i] == ' ')
      {
        j++;
      }
      else
      {
        numdata[j] = numdata[j] * 10 + (comdata[i] - '0');
      }
    }

   comdata = String("");
   Serial.print("set_time... ");
   WriteDS3231();
   Serial.println(" OK ");
   for(int i = 0; i < 7; i++)
    {
      numdata[i] = 0;
    }
    mark = 0;
  }
 Print_time();
}
void Print_time()
{
  int second,minute,hour,date,month,year,dow,temperature;
  second=Clock.getSecond();
  minute=Clock.getMinute();
  hour=Clock.getHour(h12,PM);
  date=Clock.getDate();
  month=Clock.getMonth(Century);
  year=Clock.getYear();
  dow=Clock.getDoW();

  temperature=Clock.getTemperature();
  lcd.setCursor(0, 0);
  lcd.print("20");  // Show 20 Century
    if (year>=10)    // Display year
      {
      lcd.print(year,DEC);
      }
      else
      {
      lcd.print("0");
      lcd.print(year,DEC);
      }
  lcd.print('-');

  lcd.setCursor(5, 0);
    if (month>=10)  //Display month 
      {
      lcd.print(month,DEC);
      }
      else
      {
      lcd.print("0");
      lcd.print(month,DEC);
      }
  lcd.print('-');

  lcd.setCursor(8, 0);
    if (date>=10)  // Display date
      {
      lcd.print(date,DEC);
      }
      else
      {
      lcd.print("0");
      lcd.print(date,DEC);
      }

  lcd.setCursor(11, 0);
    switch (dow)  // Display Week
      {
      case 1:  // When Dow is equal to 1, execute the following statement
        lcd.print("Mon");
        break;
      case 2:  // When Dow is equal to 2, execute the following statement
        lcd.print("Tue");
        break;
      case 3:
        lcd.print("Wed");
        break;
      case 4:
        lcd.print("Thu");
        break;
      case 5:
        lcd.print("Fri");
        break;
      case 6:
        lcd.print("Sat");
        break;
      case 7:
        lcd.print("Sun");
        break;
      }

  lcd.setCursor(0, 1);//Move the cursor to the second line.
    if (hour>=10)     //Display hours
      {
      lcd.print(hour,DEC);
      }
      else
      {
      lcd.print("0");
      lcd.print(hour,DEC);
      }
  lcd.print(':');

  lcd.setCursor(3, 1);
    if (minute>=10)  // Display minutes
      {
      lcd.print(minute,DEC);
      }
      else
      {
      lcd.print("0");
      lcd.print(minute,DEC);
      }
  lcd.print(':');

  lcd.setCursor(6, 1);
    if (second>=10)  //Display seconds
      {
      lcd.print(second,DEC);
      }
      else
      {
      lcd.print("0");
      lcd.print(second,DEC);
      }

  lcd.setCursor(12, 1);
  lcd.print(temperature);  // Display temperature
  lcd.write(0xdf);         // Display temperature symbol
  lcd.print("C");
}

