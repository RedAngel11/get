import numpy as np
import matplotlib.pyplot as plt


file_zero = 'data1.csv'  # Файл с данными при выключенном вентиляторе (P = 0 Па)
file_known = 'now.csv'  # Файл с данными при включённом вентиляторе

# давление, измеренное манометром вручную (в Паскалях)
pascal = 93

def load_data(filename):
    return np.loadtxt(filename)  # Считываем все числа из файла как массив


# Загружаем показания АЦП при нулевом давлении
adc_zero = load_data(file_zero)
# Загружаем показания АЦП при известном давлении
adc_known = load_data(file_known)

# Вычисляем среднее значение АЦП для каждого случая
avg_adc_zero = np.mean(adc_zero)  # Среднее при P = 0 Па
avg_adc_known = np.mean(adc_known)

# Выводим результаты в консоль
print(f"Среднее АЦП при P = 0 Па: {avg_adc_zero:.1f}")
print(f"Среднее АЦП при P = {pascal} Па: {avg_adc_known:.1f}")

# Создаём два списка для графика:
pressures = [0, pascal]  # Ось X: давление
adc_values = [avg_adc_zero, avg_adc_known]  # Ось Y: средние отсчёты АЦП

plt.figure(figsize=(10, 7))

plt.scatter(
    pressures,  # Координаты по оси X
    adc_values,  # Координаты по оси Y
    color='#8725C2',  # Цвет точек
    s=120,  # Размер точек (в пикселях²)
    marker='*',
    label='Измерения',  # Подпись для легенды
    zorder=5  # Поверхность: точки поверх сетки
)

# Находим коэффициенты прямой ADC = k * P + b методом наименьших квадратов
k, b = np.polyfit(pressures, adc_values, 1)  # 1 — степень полинома (прямая)

# Генерируем плавный диапазон давлений для построения прямой
P_for_plot = np.linspace(0, pascal * 1.2, 100)  # 100 точек от 0 до 1.2*P_max
ADC_fit = k * P_for_plot + b  # Вычисляем соответствующие значения АЦП по прямой
l = 1 / k
p = b / k
plt.plot(
    P_for_plot,  # Ось X: давление
    ADC_fit,  # Ось Y: расчётные значения АЦП
    color='#CF03EB',
    linewidth=2,
    label=f'P = {l:.3f}·N - {p:.2f}'
)

plt.title('Калибровочный график\n зависимости показаний АЦП от давления', fontsize=14, pad=20)
plt.xlabel('Давление $P$, Па', fontsize=12)  # Название оси X
plt.ylabel('Отсчёты АЦП $N$', fontsize=12)  # Название оси Y

plt.grid(True, which='major', alpha=0.7, linewidth=1)  # Основная сетка (толстая)
plt.grid(True, which='minor', alpha=0.4, linewidth=0.8)  # Минорная сетка (тонкая)
plt.minorticks_on()  # Включаем минорные деления

plt.legend()

# Автоматическая подгонка полей
plt.tight_layout()

plt.show()

print("\n=== Результаты калибровки ===")
print(f"Уравнение связи АЦП и давления:")
print(f"  Отсчёты АЦП: N = {k:.5f} × P + {b:.5f}")
print(f"Обратное уравнение для пересчёта в давление:")
print(f"  Давление: P = (N - {b:.5f}) / {k:.5f}  [Па]")
