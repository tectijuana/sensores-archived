/*
 * Author: SMRAZA KEEN
 * Date:2016/6/29
 * IDE V1.6.9
 * Email:TechnicSmraza@outlook.com
 * Function:
 */
int a[10][10]={
               {0,0,0,1,1,1,0,1,1,1},  //0
               {0,0,0,1,0,0,0,0,0,1},  //1
               {0,0,0,0,1,1,1,0,1,1},  //2
               {0,0,0,1,1,0,1,0,1,1},  //3
               {0,0,0,1,0,0,1,1,0,1},  //4
               {0,0,0,1,1,0,1,1,1,0},  //5
               {0,0,0,1,1,1,1,1,1,0},  //6
               {0,0,0,1,0,0,0,0,1,1},  //7
               {0,0,0,1,1,1,1,1,1,1},  //8
               {0,0,0,1,1,0,1,1,1,1},};//9  
void setup(){  
  for (int i=3;i<=9;i++) {  
    pinMode(i,OUTPUT);  
  }  
}  
void printf(int v){  
  for (int i=3;i<=9;i++){  
    digitalWrite(i,a[v][i]);  
  }  
}  
void loop(){  
  for (int i=0;i<=9;i++){  
    printf(i);  
    delay(400);  
  }  
}  
