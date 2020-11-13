int Led=13;
int tracking=3;
 
int val; 
void setup()
{ 
  pinMode(Led,OUTPUT); 
  pinMode(tracking,INPUT);
}
void loop()
{

 
val=digitalRead(tracking); 
if(val==HIGH)
{  digitalWrite(Led,HIGH); 
 }  
else
{ digitalWrite(Led,LOW);

   }
 }

