import RPi.GPIO as gg
import time

gg.setmode(gg.BCM)

led = 26
gg.setup(led, gg.OUT)

but = 13
gg.setup(but, gg.IN)

state = 0

while True:
    if gg.input(but):
        state = not state
        gg.output(led, state)
        time.sleep(0.2)
