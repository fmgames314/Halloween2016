



void setup() {
pinMode(9,OUTPUT);

}

void loop() {
  digitalWrite(9,HIGH);
  delay(random(10) );
  digitalWrite(9,LOW);
  delay(2);

}
