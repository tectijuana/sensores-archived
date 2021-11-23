/*
 * Author: SMRAZA KEEN
 * Date:2016/9/29
 * IDE V1.6.9
 * Email:TechnicSmraza@outlook.com
 * Function:Write and read card for RC522  
 * Tips:Open serial port monitor.
 * LED1 blinking and LED2 off   ->    Detecting card
 * LED1 blinking and LED2 on    ->    Waiting for write card
 * LED1 and LED2 blinking       ->    Reading card is finished
 */
#include <SPI.h>
#include <RFID.h>
const int LED1 = 3;
const int LED2 = 4;
boolean flag = false;    //Write card flag
RFID rfid(10,9);         //D10-Card Reader pin MOSI ,D9 Card Reader pin RST
//The fourth byte is card's serial number and the five byte is card's Check byte
unsigned char serNum[5];
// Write data
unsigned char writeDate[16] ={'W', 'e', 'l', 'c', 'o', 'm', 'e', 'T', 'o', 'S', 'm', 'r', 'a', 'z', 'a', 0};
//A password original sector, 16 sectors, each sector password 6Byte
unsigned char sectorKeyA[16][16] = {
        {0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF},
        {0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF},
        {0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF},};
//A password new sector, 16 sectors, each sector password 6Byte
unsigned char sectorNewKeyA[16][16] = {
        {0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF},
        {0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xff,0x07,0x80,0x69, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF},
        {0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xff,0x07,0x80,0x69, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF},};

void setup()
{
  Serial.begin(9600);
  SPI.begin();
  rfid.init();
  pinMode(LED1,OUTPUT);
  pinMode(LED2,OUTPUT);
  attachInterrupt(0, WriteCardInterrupt, RISING);   //Open external interrupt 0
}

void loop()
{ 
  unsigned char i,tmp;
  unsigned char status;
  unsigned char str[MAX_LEN];
  unsigned char RC_size;
  unsigned char blockAddr;          //Selecting operation block`s address 0～63
  //Detecting card
  rfid.isCard();
  //Reading the card serial number
  if (rfid.readCardSerial())
  {
    Serial.print("The card's number is  : ");
    Serial.print(rfid.serNum[0],HEX);
    Serial.print(rfid.serNum[1],HEX);
    Serial.print(rfid.serNum[2],HEX);
    Serial.print(rfid.serNum[3],HEX);
    Serial.print(rfid.serNum[4],HEX);
    Serial.println(" ");
  }
   //Select card and return memory size(note:Card is locked to prevent multiple read and write
   rfid.selectTag(rfid.serNum);
 
    // write data to card 
        blockAddr = 7;                //data block 7
        if(flag==true)
        { 
          if (rfid.auth(PICC_AUTHENT1A, blockAddr, sectorKeyA[blockAddr/4], rfid.serNum) == MI_OK)  //authenticate
          {
            //Write data
            status = rfid.write(blockAddr, sectorNewKeyA[blockAddr/4]);
            Serial.print("Set the new card password, and can modify the data of the Sector: ");
            Serial.println(blockAddr/4,DEC);
            //Write data
            blockAddr = blockAddr - 3 ; //data block 4
            status = rfid.write(blockAddr, writeDate);
            if(status == MI_OK)
            {
              Serial.println("Write card OK!");
              digitalWrite(LED2,LOW);   //LED lamp for writing card
              delay(1000);
              flag=false;    //Reset interrupt status
            }else{
              Serial.println("Write card Error!");
            }
          }
        }
    //Read card
    blockAddr = 7;                //data block 7
    status = rfid.auth(PICC_AUTHENT1A, blockAddr, sectorNewKeyA[blockAddr/4], rfid.serNum);
    if (status == MI_OK)  //authenticate
    {
      //Read Data
      blockAddr = blockAddr - 3 ; //data block 4
      if( rfid.read(blockAddr, str) == MI_OK)  
      {
        Serial.print("Read from the card ,the data is : ");
        Serial.println((char *)str);
        for(int j=0;j<2;j++)    // LED status for reading card
        {
        digitalWrite(LED1,HIGH);
        digitalWrite(LED2,HIGH);
        delay(500);
        digitalWrite(LED1,LOW);
        digitalWrite(LED2,LOW);
        delay(500);
        }
      }
    }
  rfid.halt();
  flashled();       // LED status for detecting card
}
void WriteCardInterrupt() //Interrupt function
{ 
  digitalWrite(LED2,HIGH);
  flag = true;
}
void flashled()
{
  digitalWrite(LED1,LOW);
  delay(200);
  digitalWrite(LED1,HIGH);
  delay(200);
  Serial.println("Detecting card........");
}
