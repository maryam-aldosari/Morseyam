
import machine
import time

led = machine.Pin(14, machine.Pin.OUT)

pause = 100
letters = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..",
          "j":".---","k": "-.-", "l":".-..", "m":"--", "n":"-.", "o":"---", "p":".--.","q": "--.-","r": ".-.",
           "s":"...", "t":"-","u":"..-","v":"...-","w":".--","x": "-..-","y": "-.--","z": "--.."}
#message = "hello my name is maryam"

def send_message(message):
  for char in message:
    if char == " ":
      time.sleep_ms(pause*4)
    else:
      for code in letters[char]:
        led.value(1)
        #print(code)
        if code == ".":
          time.sleep_ms(pause)
        else:
          #print("dash")
          time.sleep_ms(pause*3)
        led.value(0)
        time.sleep_ms(pause)
      time.sleep_ms(pause*2)

"""
const int pause = 50;

const String letters[] = {
  ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", // a-i
  ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", // j-r
  "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."         // s-z
};

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin 9 as an output.
  pinMode(9, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  String message = "hello my name is maryam";
  for (char ch: message) {
    if (ch == ' '){
      delay(pause * 4); //pause between words
    }
    else{
      flashLetter(letters[ch - 'a']);
      delay(pause * 2); // pause between letters
    }

  }
  exit(0);
}

void flashLetter(String code){
  for (char ch: code) {
    digitalWrite(9, HIGH);
    if (ch == '.'){ //delay for dot 
      delay(pause);
    }
    else{ //delay for dash
      delay(pause * 3);
    }

    digitalWrite(9, LOW);
    delay(pause);
    
  }
"""