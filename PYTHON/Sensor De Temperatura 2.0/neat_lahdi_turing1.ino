int LED = 7;
int TMP = 0;
float temperatura = 0;

void setup()
{
 	pinMode(LED, OUTPUT); 
}

void loop()
{
	temperatura = map(analogRead(TMP),0,1023,-50,450);


	if (temperatura>= 25)
	{
  		digitalWrite(LED,HIGH);
	}

	else
	{
  		digitalWrite(LED,LOW);
	}
  
  	delay (10);
	
}