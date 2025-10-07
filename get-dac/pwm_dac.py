import RPi.GPIO as gg

class PWM_DAC:
    def __init__(self, gpio_pin, freq, range, verbose = True):
        self.gpio_pin = gpio_pin
        self.freq = freq
        self.range = range
        self.verbose = verbose
        # Настройка GPIO
        gg.setmode(gg.BCM)
        gg.setup(self.gpio_pin, gg.OUT, initial=gg.LOW)
        # важная деталь
        self.pwm = gg.PWM(self.gpio_pin, self.freq)
        self.pwm.start(0)

    def deinit(self):
        """Сброс всех пинов и отключение GPIO""" 
        gg.output(self.gpio_pin, gg.LOW)
        gg.cleanup()
# duty - это процент времени, когда сигнал максимален (HIGH)
    def voltage_to_duty(self, voltage): #перевести напряжение в скважность
        if voltage <= 0:
            duty = 0
        elif voltage >= self.range:
            duty = 100
        else: # и наконец 
            duty = int((voltage / self.range) * 100)
        return duty

    def set_output(self, duty):# тут надо реализовать 
        self.pwm.ChangeDutyCycle(duty)

        if self.verbose: # показываем пользователю, что у нас получилось, если флаг врублен
            print(f"→ Вых. скважность.: {duty:.2f}")

# =================== НАЧИНАЕТСЯ САМА ПРОГРАММА ===================
if __name__ == "__main__":
    pwm = None
    try:
        # Создаём объект ЦАП
        pwm = PWM_DAC(
            gpio_pin = 21,  # BCЕ номера пинов в нашем конкретном случае
            freq = 500, # частота - сколько раз в секунду повторяется полный цикл H и L
            range = 3.17 , # опорное напряжение
            verbose = True # флажочек
        )

        while True:
            try: # получаем напряжение от пользователя, квантуем, передаем на пины
                voltage = float(input("\nВведите аналоговое напряжение от 0 до 3.17 В:  "))
                duty = pwm.voltage_to_duty(voltage)
                pwm.set_output(duty)
            except ValueError:
                print("введите нормальное float число - аналоговое напряжение ")

    finally:# выключаем ЦАП
        if pwm is not None:
            pwm.deinit()
        else:
            print("Ксюша, у тебя не работает обьект pwm")