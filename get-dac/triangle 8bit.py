import r2r_dac as r2r
import signal_generator as sg
import time

amplitude = 3.17
signal_frequency = 10
sampling_frequency = 100

if __name__ == "__main__":
    try:
        dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.17, True)

        while True:
            # Получаем нормализованное значение синуса от 0 до 1
            sin_value = sg.get_sin_wave_A(signal_frequency, time.time())      
            voltage = sin_value * amplitude  # Преобразуем в напряжение      
            # Отправляем на ЦАП
            code = dac.voltage_to_code(voltage)
            dac.set_output(code)
            # Ждём следующий период дискретизации
            sg.wait_for_sampling_period(sampling_frequency)
    finally:
        dac.deinit()