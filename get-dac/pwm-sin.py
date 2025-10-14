import pwm_dac as pwm
import signal_generator as sg
import time

amplitude = 3.2          # Вольты
signal_frequency = 100   # Гц частота синусоиды(меньше сотни не видно всю волну)
sampling_frequency = 1000 # частота дискретизации
dac = None

try:
    # Создаём объект 
    dac = pwm.PWM_DAC(
        gpio_pin= 12,
        freq = sampling_frequency,
        range = 3.17,                            # опорное напряжение
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
        duty = dac.voltage_to_duty(voltage)
        dac.set_output(duty)
        # Ждём следующий период дискретизации
        sg.wait_for_sampling_period(sampling_frequency)
finally:
    if dac is not None:
        dac.deinit()