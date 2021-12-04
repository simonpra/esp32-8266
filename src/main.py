# This is your main script.
from time import sleep
from machine import Pin

### READ-TEMPERATURE
from readTemp import readTemp, sendTemp

### IMPORT pour le WIFI
from wifi.wifiConnect import connect
### connect to PrakyNet
connect()

led = Pin(2, Pin.OUT)


while True:
    led.value( 0x0 )
    sendTemp( 'https://www.ized.ch/temp/temperature/' )
    led.value( 0x1 )
    sleep(59)
