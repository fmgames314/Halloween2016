


byte magnetoSen = A0;

void setup() 
{
pinMode(magnetoSen,INPUT);
pinMode(9,OUTPUT);
}


int magnetoFlipFlop = 0;
int motorClick = 0;
void loop() 
{
  int magnetoAVGvalue = analogRead(magnetoSen);
  if(magnetoAVGvalue > 50 && magnetoFlipFlop == 1 )
  {
  motorClick+=1;
  magnetoFlipFlop = !magnetoFlipFlop;
  digitalWrite(9,LOW);
  }
  if(magnetoAVGvalue < 30 && magnetoFlipFlop == 0 )
  {
  magnetoFlipFlop = !magnetoFlipFlop;
  digitalWrite(9,HIGH);
  }
  

}
