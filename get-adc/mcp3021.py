import smbus as sm
import time
class MCP:
    def __init__(self, range, verbose = False):
        self.bus = sm.SMBus(1)# номер шины 
        self.address = 0x4D # адрес микросхемы
        self.verbose = verbose
        self.range = range
    def deinit(self):
        self.bus.close()
    def get_number(self):
    
        # Читаем слово (2 байта) по адресу устройства
        data = self.bus.read_word_data(self.address, 0)

        # Разбираем на байты:
        # Внимание! I2C на Pi может возвращать байты в обратном порядке
        lower_data_byte = data >> 8      # Старший байт слова — это младший байт передачи
        upper_data_byte = data & 0xFF    # Младший байт слова — это старший байт передачи

        number = (upper_data_byte << 6) | (lower_data_byte >> 2)

        if self.verbose:
            print(f"Принятое слово: {data} ({data})")
            print(f"Старший байт (upper): {upper_data_byte:x}, "
                  f"Младший байт (lower): {lower_data_byte:x}")
            print(f"Число: {number}")

        return number

    def get_voltage(self):

        dig = self.get_number()
        voltage = dig / 1023 * self.range
        return voltage       

# =================== НАЧИНАЕТСЯ САМА ПРОГРАММА ===================
if __name__ == "__main__":
    try:
        adc = MCP(3.258, False)

        while True:
            voltage = adc.get_voltage()
            print(f"Напряжение: {voltage:.3f} В")
            time.sleep(1.0)  # Чтобы не перегружать терминал

    except KeyboardInterrupt: print("\nЗавершено пользователем.")
    finally: adc.deinit()  # Закрываем шину