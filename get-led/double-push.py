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

num = 100
sleep_time = 0.2

def dec(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

while True:
    for led in leds:
        if gg.input(up and down):
            num = 255
            pr = dec(num)
            for i in range(0,8):
                if pr[i]==1: gg.output(leds[i], 1)
                if pr[i]==0: gg.output(leds[i], 0)
            time.sleep(sleep_time)            
        if gg.input(up):
            if num < 255: num = num +1
            if num == 255: num = 0 
            pr = dec(num)
            print(num, dec(num))
            for i in range(0,8):
                if pr[i]==1: gg.output(leds[i], 1)
                if pr[i]==0: gg.output(leds[i], 0)
            time.sleep(sleep_time)


        if gg.input(down):
            if num> 0: num = num - 1
            pr = dec(num)
            print(num, dec(num))
            for i in range(0,8):
                if pr[i]==1: gg.output(leds[i], 1)
                if pr[i]==0: gg.output(leds[i], 0)
            time.sleep(sleep_time)

