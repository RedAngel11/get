import RPi.GPIO as gg

class R2R_DAC:
    def __init__(self, gpio_pins, range, verbose=True):
        self.gpio_pins = gpio_pins
        self.range = range
        self.verbose = verbose
        self.num_bits = len(gpio_pins)
        # Настройка GPIO
        gg.setmode(gg.BCM)
        gg.setup(self.gpio_pins, gg.OUT, initial=gg.LOW)

    def deinit(self):
        """Сброс всех пинов и отключение GPIO"""
        gg.output(self.gpio_pins, gg.LOW)
        gg.cleanup()

    def voltage_to_code(self, voltage):
        if voltage <= 0:
            code = 0
        elif voltage >= self.range:
            code = 255
        else:
            code = int((voltage / self.range) * 255)
        return code

    def set_output(self, code):
        # Переводим в двоичное
        bits = [int(bit) for bit in bin(code)[2:].zfill(self.num_bits)]

        # Подаем бит на пин
        for pin, value in zip(self.gpio_pins, bits):#зип сопоставляет два
            gg.output(pin, value)
        if self.verbose:
            voltage_out = code / 255 * self.range
            print(f"→ Вых. напр.: {voltage_out:.2f} В | в квантах: {code} | в битах: {bits}")



# =================== ОСНОВНАЯ ПРОГРАММА ===================
if __name__ == "__main__":
    try:
        # Создаём объект ЦАП
        dac = R2R_DAC(
            gpio_pins=[16, 20, 21, 25, 26, 17, 27, 22],  # BCM номера пинов
            range=3.183,  # опорное напряжение
            verbose=True
        )

        while True:
            try:
                voltage = float(input("\nВведите напряжение от 0 до 3.183 В:  "))
                code = dac.voltage_to_code(voltage)
                dac.set_output(code)
            except ValueError:
                print("введите число ")

    finally:
        dac.deinit()