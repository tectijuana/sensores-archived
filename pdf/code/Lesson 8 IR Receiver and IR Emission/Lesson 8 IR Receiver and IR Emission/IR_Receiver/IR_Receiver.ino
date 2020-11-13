
//www.elegoo.com
//2017.12.16
 #include <IRremote.h>
 #define RECV_PIN  11        //Infrared signal receiving pin
 #define LED       13        //define LED pin
 IRrecv irrecv(RECV_PIN);
 decode_results results;
 void setup()
 { 
   pinMode(LED, OUTPUT); //initialize LED as an output
   Serial.begin(9600);
   irrecv.enableIRIn(); // Start the receiver
 }
  void loop() 
 {
  if (irrecv.decode(&results)) 
   { 
     int state;
       if ( results.value == 1 )  
       {    
         state = HIGH;
       }
       else
       {
        state = LOW;
       }
    digitalWrite( LED, state );     
    Serial.println(results.value);
    irrecv.resume();        // prepare to receive the next value
   }
 }
