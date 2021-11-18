# This is your main script.
from time import sleep
from machine import Pin

led = Pin(2, Pin.OUT)

while True:
    led.value( not led.value() )
    sleep(0.5)
