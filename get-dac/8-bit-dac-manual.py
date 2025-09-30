import RPi.GPIO as gg

gg.setmode(gg.BCM)
pins = [16,20,21,25, 26,17,27,22]
gg.setup(pins, gg.OUT)


dynamic_range = 3.1

def voltage_to_number(voltage):#НАПРЯЖЕНИЕ КВАНТУЕТСЯ В ЧИСЛО от 0 до 2^8=255
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение вне динамического диапазона ЦАП 0.00 - {dynamic_range:.2f} B")
        print("Ставим 0.0 В")
        return 0
    return int(voltage/dynamic_range*255)
def dec(value):#ПОЛУЧИВШЕЕСЯ ДЕСЯТИЧНОЕ В ДВОИЧНОЕ ЧИСЛО
    return [int(element) for element in bin(value)[2:].zfill(8)]
def number_to_dac(bin_num):#ПОДАТЬ ДВОИЧНОЕ ЧИСЛО НА ВЫХОД 
    print(f"Число на вход ЦАП {number} - в двоичном виде {bin_num}")
    for pin in pins:
        pr = bin_num
        for i in range(0,8):
                if pr[i]==1: gg.output(pins[i], 1)
                if pr[i]==0: gg.output(pins[i], 0)

    return 0

try:#САМА РАБОТА ПРОГРАММЫ: 
    while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах "))#ввод
            number = voltage_to_number(voltage)#ПЕРЕквантовали напряжение
            bin_num = dec(number)#перевели в двоичное
            number_to_dac(bin_num)#передали двоичное на плату
        except ValueError:
            print("Ты ввел фигню, попробуй еще раз\n")
finally:
    gg.output(pins, 0)
    gg.cleanup()