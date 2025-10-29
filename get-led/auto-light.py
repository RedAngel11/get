import RPi.GPIO as gg
import time

gg.setmode(gg.BCM)

led = 26
gg.setup(led, gg.OUT)

foto = 6
gg.setup(foto, gg.IN)

while True:
    gg.output(led, not gg.input(foto))