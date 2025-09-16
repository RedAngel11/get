import RPi.GPIO as gg
import time

gg.setmode(gg.BCM)

leds = [24, 22, 23, 27, 17, 25, 12, 16]
gg.setup(leds, gg.OUT)
gg.output(leds, 0)

light_yime = 0.2

while True:
    for led in leds:
        gg.output(led, 1)
        time.sleep(light_yime)
        gg.output(led, 0)
    for led in reversed(leds):
        gg.output(led, 1)
        time.sleep(light_yime)
        gg.output(led, 0)
    time.sleep(light_yime)
