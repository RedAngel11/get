import smbus as sm

class MCP:
    def __init__(self, range, adress = 0x61, verbose = True):
            self.bus = sm.SMBus(1)# номер шины 

            self.adress = adress # адрес микросхемы
            self.wm = 0x00
            self.pds = 0x00
            self.verbose = verbose
            self.range = range


    def deinit(self):
        self.bus.close() 

    def set_number(self, number): # отправляет три байта
        if not isinstance(number, int):
         print("На вход ЦАП можно подавать только целые числа")

        if not (0 <= number <= 4095):
            print("Число выходит за разрядность MCP4752 (12 бит)")

        first_byte = self.wm | self.pds | number >> 8
        second_byte = number & 0xFF
        self.bus.write_byte_data(0x61, first_byte, second_byte)

        if self.verbose:
            print(f"Число: {number}, отправленные по I2C данные: [0x{(self.adress << 1):02X}, 0x{first_byte:02X}, 0x{second_byte:02X}]\n")
    
    def set_voltage(self, voltage): # напряжение в число 0-4095
        if voltage < 0:
            voltage = 0
        elif voltage > self.range:
            voltage = self.range

        number = int((voltage / self.range) * 4095)
        self.set_number(number)


# =================== НАЧИНАЕТСЯ САМА ПРОГРАММА ===================
if __name__ == "__main__":
    mcp = None
    try:
        # Создаём объект ЦАП
        mcp = MCP(
            range = 5.18 , # опорное напряжение
            adress = 0x61,
            verbose = True # флажочек
        )

        while True:
            try: # получаем напряжение от пользователя, квантуем, передаем на пины
                voltage = float(input("\nВведите аналоговое напряжение от 0 до 5.18 В:  "))
                
                mcp.set_voltage(voltage)
            except ValueError:
                print("введите нормальное float число - аналоговое напряжение ")

    finally:# выключаем ЦАП
        if mcp is not None:
            mcp.deinit()
        else:
            print("Ксюша, у тебя не работает обьект mcp")