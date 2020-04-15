/*
 * Author: SMRAZA KEEN
 * Date:2016/6/29
 * IDE V1.6.9
 * Email:TechnicSmraza@outlook.com
 * Function:
 */
 #include <dht11.h>                  
dht11 DHT;                  //Note: DHT on behalf of the DHT11 sensor 
const int dht11_data = 8;     //Please put the DH11`s dht11_data pin connect with arduino digital Port 8
int temp=0;
int hum=0;
void setup()
{
  Serial.begin(9600);
}
void loop()
{ 
  DHT.read(dht11_data);
  temp=DHT.temperature;
  hum=DHT.humidity;
  Serial.print("Hum=\t%");            
  Serial.print(hum);
  Serial.print("\tTemp=\t");            
  Serial.println(temp);
  delay(1000);
}

