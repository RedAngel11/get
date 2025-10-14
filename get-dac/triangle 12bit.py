import mcp4725 as mcp
import signal_generator as sg
import time

amplitude = 5.15
signal_frequency = 10
sampling_frequency = 100

if __name__ == "__main__":
    try:
        mcp = mcp.MCP(5.15, True)

        while True:
            sin_value = sg.get_sin_wave_A(signal_frequency, time.time())      
            voltage = sin_value * amplitude
            mcp.set_voltage(voltage)
            sg.wait_for_sampling_period(sampling_frequency)

    finally:
        mcp.deinit()