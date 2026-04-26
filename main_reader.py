from machine import ADC, Pin
import time 

pot = ADC(Pin(14))

pot.atten(ADC.ATTN_11DB)  
led_on = False
led_threshold = 2.35
pause = 100
timer = time.ticks_ms()

letters ={".-":"a","-...":"b","-.-.":"c","-..":"d",".":"e","..-.":"f","--.":"g","....":"h","..":"i",
           ".---":"j","-.-":"k",".-..":"l","--":"m","-.":"n","---":"o",".--.":"p","--.-":"q",".-.":"r",
           "...":"s","-":"t","..-":"u","...-":"v",".--":"w","-..-":"x","-.--":"y","--..":"z"} 
letter = ""
while True:
    value = pot.read()  
    voltage = (value * 3.3) / 4095  
    #print(f"Voltage: {voltage:.2f} V")
    if len(letter) > 0 and not led_on and round(time.ticks_diff(time.ticks_ms(), timer)/ pause) > 2:
      if letter in letters:
        print(letters[letter], end = "")
      else:
        print("?")
      letter = ""
    if led_on and voltage < led_threshold:
      #print("led_turned_off")
      blink = round(time.ticks_diff(time.ticks_ms(), timer)/ pause)
      #print("blinked_for ", blink)
      if blink == 1:
        #print(".", end = "")
        letter += "."
      elif blink ==3:
        #print("-", end = "")
        letter += "-"
      timer = time.ticks_ms()
      led_on = False
    elif not led_on and voltage > led_threshold:
      #print("led_turned_on")
      paused = round(time.ticks_diff(time.ticks_ms(), timer)/ pause)
      #print("paused_for ", paused)
      
      #if paused == 3:
        #print(" ", end = "")
        #continue
      if paused >= 7:
        #print(" / ", end = "")
        print(" ", end = "")
        
      timer = time.ticks_ms()
      led_on = True
    time.sleep(0.01)  