import RPi.GPIO as gg
import time

gg.setmode(gg.BCM)

led = 26
gg.setup(led, gg.OUT)

foto = 6
gg.setup(foto, gg.IN)
state = 0

while True:
    if gg.input(foto):
        state = not state
        gg.output(led, state)
        time.sleep(0.5)