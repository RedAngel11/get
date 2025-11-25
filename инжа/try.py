from matplotlib import pyplot as plt
import numpy as np

Q = []
with open("consumption.txt") as file:
    for line in file:
        c = float(line)
        Q.append(c)

X = [0, 10, 20, 30, 40, 50, 60, 70]

fig, ax = plt.subplots(figsize=(10,7))
ax.plot(
    X,
    Q,
    label='расход Q(r) для 0-70 мм',
    linestyle='--',
    color='#CF20FF'
)
ax.scatter(
    X,
    Q,
    color='#AC29E0',
    s = 120,
    marker='*',
    zorder=5
)

ax.minorticks_on()
ax.grid(which='major', linewidth = 1)
ax.grid(which='minor', linestyle = ':')

# Преобразуем списки в numpy массивы
X_array = np.array(X)
Q_array = np.array(Q)

# Линейная аппроксимация: Q = a * X + b
coefficients = np.polyfit(X_array, Q_array, 1)  # степень полинома = 1
a, b = coefficients

# Создаем точки для линии аппроксимации
X_smooth = np.linspace(min(X), max(X), 100)
Q_fit = a * X_smooth + b

# Добавляем линию МНК на график
ax.plot(
    X_smooth,
    Q_fit,
    color='#1E9E4A',
    linewidth=2,
    linestyle='-',
    label=f'Q(r) = {a:.4f}·r + {b:.4f}'
)

ax.set_xlabel("Расстояние от трубки Пито до сопла, мм")
ax.set_ylabel("Расход, г/с")
ax.set_title("График зависимости расхода от расстояния до сопла")
ax.legend()
plt.show()
