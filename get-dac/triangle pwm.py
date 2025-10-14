import pwm_dac as pwm
import signal_generator as sg
import time

amplitude = 3.16
signal_frequency = 10
sampling_frequency = 100

if __name__ == "__main__":
    try:
        pwm = pwm.PWM_DAC(12, 500, 3.16, True)

        while True:
            sin_value = sg.get_sin_wave_A(signal_frequency, time.time())      
            voltage = sin_value * amplitude 
            duty = pwm.voltage_to_duty(voltage)
            pwm.set_output(duty)           
            sg.wait_for_sampling_period(sampling_frequency)

    finally:
        pwm.deinit()