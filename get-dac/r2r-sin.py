# import r2r_dac as r2r
# import signal_generator as sg
# import time 

# A = 3.2
# si_freq = 10
# samp_freq = 1000
import r2r_dac as r2r
import signal_generator as sg
import time

# Параметры сигнала
amplitude = 3.2          # Вольты
signal_frequency = 10    # Гц (частота синусоиды)
sampling_frequency = 1000  # Гц (сколько точек в секунду)

# =================== ОСНОВНАЯ ПРОГРАММА ===================
dac = None

try:
    # Создаём объект ЦАП (предполагаем, что у тебя есть файл r2r_dac.py с классом R2R_DAC)
    dac = r2r.R2R_DAC(
        gpio_bits=[16, 20, 21, 25, 26, 17, 27, 22],  # BCM номера пинов
        dynamic_range=3.3,                            # опорное напряжение
        verbose=False                                 # можно включить для отладки
    )

    print(f"[SINUS] Генерация синусоиды: {signal_frequency} Гц, амплитуда {amplitude} В, дискретизация {sampling_frequency} Гц")

    start_time = time.time()  # начальное время

    while True:
        current_time = time.time() - start_time  # прошедшее время

        # Получаем нормализованное значение синуса от 0 до 1
        sin_value = sg.get_sin_wave_amplitude(signal_frequency, current_time)

        # Преобразуем в напряжение
        voltage = sin_value * amplitude

        # Отправляем на ЦАП
        dac.set_voltage(voltage)

        # Ждём следующий период дискретизации
        sg.wait_for_sampling_period(sampling_frequency)

except KeyboardInterrupt:
    print("\n\n👋 Сигнал остановлен пользователем.")
finally:
    if dac is not None:
        dac.deinit()