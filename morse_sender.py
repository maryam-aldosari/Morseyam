
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

