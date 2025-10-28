# r2r_adc.py (обновлённая версия)

import RPi.GPIO as GPIO
import time

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time=0.01, verbose=False):
        self.dynamic_range = dynamic_range
        self.compare_time = compare_time
        self.verbose = verbose
        
        # Пины ЦАПа: [GPIO26, ..., GPIO11] — 8 пинов
        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21  # Выход компаратора

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial=0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def __del__(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()

    def number_to_dac(self, number):
        """Подаёт 8-битное число на ЦАП"""
        bits = [(number >> i) & 1 for i in range(7, -1, -1)]
        GPIO.output(self.bits_gpio, bits)
        time.sleep(self.compare_time)

    # --- Новые методы для АЦП последовательного приближения ---

    def successive_approximation_adc(self):
        """
        Реализует алгоритм последовательного приближения (SAR).
        Определяет значение напряжения, устанавливая биты от старшего к младшему.
        """
        digital_value = 0  # Начальное значение: все биты 0

        # Обрабатываем каждый бит, начиная со старшего (бит 7)
        for bit in range(7, -1, -1):
            # Устанавливаем текущий бит в 1, младшие — в 0
            candidate = digital_value | (1 << bit)  # Пробуем установить бит
            self.number_to_dac(candidate)

            # Читаем результат сравнения
            comp_output = GPIO.input(self.comp_gpio)

            if comp_output == 0:
                # Входное напряжение >= U_DAC → оставляем бит установленным
                digital_value = candidate
            else:
                # U_DAC > входного → сбрасываем бит (он остаётся 0)
                pass

            if self.verbose:
                print(f"Бит {bit}: {'1' if (digital_value >> bit) & 1 else '0'}, comp={comp_output}")

        return digital_value

    def get_sar_voltage(self):
        """Возвращает напряжение в вольтах, измеренное SAR-методом"""
        digital_value = self.successive_approximation_adc()
        voltage = digital_value / 255 * self.dynamic_range
        return voltage


# === ОСНОВНОЙ ОХРАННИК ===
if __name__ == "__main__":
    try:
        # Измерь DYNAMIC_RANGE мультиметром!
        adc = R2R_ADC(dynamic_range=3.3, compare_time=0.001, verbose=False)
        
        print("Измерение напряжения с помощью SAR-АЦП...")
        print("Нажми Ctrl+C для выхода")
        
        while True:
            voltage = adc.get_sar_voltage()
            print(f"Напряжение: {voltage:.3f} В")
            time.sleep(0.1)  # Можно уменьшить или убрать
            
    except KeyboardInterrupt:
        print("\nЗавершено пользователем.")
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        del adc