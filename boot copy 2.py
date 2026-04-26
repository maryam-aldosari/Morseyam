
#import esp
#esp.osdebug(None)
import webrepl
webrepl.start()


#import esp
#esp.osdebug(None)
import webrepl
webrepl.start()

import network
import time
import webrepl


SSID = '905@Vantage'
PASSWORD = 'X10rYHkhGzCI'

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Connecting to WiFi...')
        wlan.connect(SSID, PASSWORD)
        while not wlan.isconnected():
            time.sleep(1)
            pass
    
    # The first item in the tuple is the IP address
    ip_address = wlan.ifconfig()[0]
    print('Connected! Network config:', wlan.ifconfig())
    print(f'Your ESP32 IP Address is: {ip_address}')

connect_wifi()

# Start the WebREPL server
webrepl.start()
