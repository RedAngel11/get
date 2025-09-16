import RPi.GPIO as gg
import time

gg.setmode(gg.BCM)
leds = [16, 12, 25, 17, 27, 23, 22, 24]

gg.setup(leds, gg.OUT)
gg.output(leds, 0)

up = 9
down = 10
gg.setup(up, gg.IN)
gg.setup(down, gg.IN)

num = 250
sleep_time = 0.2

def dec(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

while True:
    if gg.input(up):
        if num < 255: num = num +1
        print(num, dec(num))
        time.sleep(sleep_time)

    if gg.input(down):
        if num> 0: num = num - 1
        print(num, dec(num))
        time.sleep(sleep_time)

