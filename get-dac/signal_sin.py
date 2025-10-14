import numpy as np
import time
import math

def get_sin_wave_A(freq, t):
    raw = np.sin(2* np.pi * freq * t)
    norm = (raw + 1)/2 # нормируем из-за особеностей проги
    return norm
def wait_for_sampling_period(samp_freq):
    period = float (1.0 / samp_freq)
    time.sleep(period)

def get_triangle(freq, time):
    return 2*abs(freq*time - math.floor(freq*time) - 0.5)
