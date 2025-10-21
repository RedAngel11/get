import RPi.GPIO as gg
import time

class R2R_ADC:
    def __init__(self, range, compare_time = 0.01, verbose = False):
        self.range = range
        self.verbose = verbose
        self.compare_time = compare_time

        self.pins_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        gg.setmode(gg.BCM)
        gg.setup(self.pins_gpio, gg.OUT, initial = 0)
        gg.setup(self.comp_gpio, gg.IN)

    def deinit(self):
        gg.output(self.pins_gpio, 0)
        gg.cleanup()
    
    def num_to_dac(self, number):#число в биты, биты на пины
        bits = [int(element) for element in bin(number)[2:].zfill(8)]
        gg.output(self.pins_gpio, bits)
        time.sleep(self.compare_time)

    def seq_count_adc(self): # выход - это число
        for num in range(256):
            self.num_to_dac(num)#подать число на ЦАП
            comp_value = gg.input(self.comp_gpio)#результат сравнения на компараторе
            if comp_value == 1: return num # если да, то останавливаем перебор

        return 255# если так и не превысило - максимум

    def binary_search_adc(self):
        low = 0
        high = 255
        while low < high:
            mid = (low + high) // 2
            self.num_to_dac(mid)
            
            if gg.input(self.comp_gpio) == 1:
                high = mid - 1
            else:
                low = mid + 1
        
        return high if high >= 0 else 0
    
    def get_sc_voltage(self): # число в напряжение
        dig = self.binary_search_adc()
        voltage = dig / 255 * self.range
        return voltage

# =================== НАЧИНАЕТСЯ САМА ПРОГРАММА ===================
if __name__ == "__main__":
    try:
        adc = R2R_ADC(3.281, 0.01, False)

        while True:
            voltage = adc.get_sc_voltage()
            print(f"Напряжение: {voltage:.3f} В")
            time.sleep(0.1)

    except KeyboardInterrupt: print("\n Ты выключила программу")
    finally: adc.deinit()

