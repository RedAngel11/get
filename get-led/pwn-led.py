import RPi.GPIO as gg
import time

gg.setmode(gg.BCM)

led = 26
gg.setup(led, gg.OUT)

pwm = gg.PWM(led, 200)
duty = 0.0
pwm.start(duty)
#state = 0

while True:
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.05)

    duty += 1.0
    if duty > 100.0:
        duty = 0.0