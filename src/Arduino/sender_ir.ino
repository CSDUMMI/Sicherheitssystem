#include <IRremote.h>
IRsend irsend;
 
void setup()
{

}

void loop() {irsend.sendRC5(16743993, 10);
           delay(10000);}
