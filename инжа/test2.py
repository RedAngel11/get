import numpy as np
import matplotlib.pyplot as plt

P_k = 96.22261
P_0 = 214572.63 / P_k
ro = 1.2
deltr_mm = 0.057


def load_data(filename):
    """Загружает данные и возвращает ADC, X, V"""
    with open(filename) as f:
        data = [int(line.strip()) for line in f if line.strip()]

    # Создаем координаты X
    X = np.array([i * deltr_mm for i in range(len(data))])

    # Вычисляем давление и скорость
    pressure = np.array(data) / P_k - P_0
    V = np.sqrt(2 * np.maximum(pressure, 0) / ro)

    return data, X, V


# Построим графики для всех сечений
distances = [0, 10, 20, 30, 40, 50, 60, 70]
plt.figure(figsize=(15, 10))

for i, dist in enumerate(distances):
    filename = f"{dist}.csv"
    try:
        adc, X, V = load_data(filename)

        # Находим центр струи (по максимуму скорости)
        max_idx = np.argmax(V)
        center = X[max_idx]

        # Центрируем
        X_centered = X - center

        # Строим график
        plt.subplot(2, 4, i + 1)
        plt.plot(X_centered, V, 'g', linewidth=1.5)
        plt.axvline(x=0, color='b', linestyle='--', label='Центр струи')
        plt.title(f'{dist} мм')
        plt.xlabel('X [мм]')
        plt.ylabel('V [м/с]')
        plt.grid(True)
        plt.ylim(0, 15)
        plt.legend()

    except FileNotFoundError:
        print(f"Файл {filename} не найден")

plt.tight_layout()
plt.show()