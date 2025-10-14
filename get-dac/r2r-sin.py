import r2r_dac as r2r
import signal_generator as sg
import time

# Параметры сигнала
amplitude = 3.2            # Вольты
signal_frequency = 100   # Гц частота синусоиды(меньше сотни не видно всю волну)
sampling_frequency = 1000  # Гц сколько точек в секунду(больше 1000 не ставить)
#если ставить слишком много точек, то будет вылетать часто
#но из-за того, что их мало, у нас много бугорочков на графике
# =================== ОСНОВНАЯ ПРОГРАММА ===================
dac = None

try:
    # Создаём объект ЦАП (юзаем r2r_dac с классом R2R_DAC)
    dac = r2r.R2R_DAC(
        gpio_pins=[16, 20, 21, 25, 26, 17, 27, 22],  # BCM номера пинов
        range = 3.3,                            # опорное напряжение
        verbose = True                           # можно включить для отладки
    )

    print(f"[SINUS] Генерация синусоиды: {signal_frequency} Гц, амплитуда {amplitude} В, дискретизация {sampling_frequency} Гц")

    start_time = time.time()  # начальное время

    while True:
        current_time = time.time() - start_time  # прошедшее время

        # Получаем нормализованное значение синуса от 0 до 1
        sin_value = sg.get_sin_wave_A(signal_frequency, current_time)      
        voltage = sin_value * amplitude  # Преобразуем в напряжение      
        # Отправляем на ЦАП
        code = dac.voltage_to_code(voltage)
        dac.set_output(code)
        # Ждём следующий период дискретизации
        sg.wait_for_sampling_period(sampling_frequency)
finally:
    if dac is not None:
        dac.deinit()