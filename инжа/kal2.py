import numpy as np
import matplotlib.pyplot as plt

steps = [0, 1500]          # Количество шагов двигателя
displacement_cm = [0, 8.35]# Перемещение трубки Пито в сантиметрах

plt.figure(figsize=(10, 7))

plt.scatter(
    steps,                 # Ось X: количество шагов
    displacement_cm,       # Ось Y: перемещение в см
    color='#801FFF',       # Цвет точек
    marker='*',            # Форма маркера — звезда
    s=100,                 # Размер маркера
    label='Измерения',     # Подпись для легенды
    zorder=5  # точки поверх сетки
)

# Линейная аппроксимация
k, b = np.polyfit(steps, displacement_cm, 1)

steps_plot = np.linspace(0, max(steps), 100) # 100 точек от 0 до максимального шага
disp = k * steps_plot + b     # Вычисляем соответствующее перемещение

plt.plot(
    steps_plot,           # Ось X: шаги
    disp,         # Ось Y: рассчитанное перемещение
    color='#D184FF',           # Цвет линии
    linewidth=2,              # Толщина линии
    label=f'X = {k:.1e} * step [см]'  # Подпись с формулой (в см!)
)

plt.title('Калибровочный график\nзависимости перемещения трубки Пито от шага двигателя', fontsize=14, pad=20)
plt.xlabel('Количество шагов', fontsize=12)               # Название оси X
plt.ylabel('Перемещение трубки Пито [см]', fontsize=12)   # Название оси Y

plt.grid(True, which='major', alpha=0.7, linewidth=1)     # Основная сетка
plt.grid(True, which='minor', alpha=0.4, linewidth=0.8)   # Минорная сетка
plt.minorticks_on()  # Включаем минорные деления

plt.legend()
plt.tight_layout()
plt.show()

print(f"Уравнение: X = {k:.6f} * step + {b:.6f} [см]")
print(f"Коэффициент пропорциональности: {k:.6f} см/шаг")
