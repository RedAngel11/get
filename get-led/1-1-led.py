import RPi.GPIO as ggg
import time

ggg.setmode(ggg.BCM)

led = 26
ggg.setup(led, ggg.OUT)
state = 0
period = 1.0

while True:
    ggg.output(led, state)
    state = not state
    time.sleep(period)