from machine import Pin
import time

leds = [Pin(i, Pin.OUT)for i in (13, 12, 14, 27, 26, 25, 33, 32)]

veces = 0

while veces < 3:
    for led in leds:
        led.value(1)
        time.sleep(0.4)
        led.value(0)
    for led in reversed (leds):
        led.value(1)
        time.sleep(0.4)
        led.value(0)
    veces += 1
