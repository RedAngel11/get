from matplotlib import pyplot as plt
import numpy as np

# Переводим в формат, используемый в коде старшекурсников
P_k = 89.691  # ≈ 90.909
P_0 = 214572.6/P_k  # ≈ 217487.27

# --- ДОПОЛНИТЕЛЬНЫЕ ПАРАМЕТРЫ ---
ro = 1.34  # Плотность воздуха (кг/м³)
deltr = 0.56  # Шаг измерения в мм (500 шагов = 28.5 мм => 0.057 см/шаг * 10 шагов/мм = 0.57 мм)
# (У них 0.45 мм)

# Рассчитываем количество точек (от -30 до +30 мм)
count = int(60 / deltr) + 1


# --- ОБРАБОТКА ДАННЫХ ДЛЯ КАЖДОГО СЕЧЕНИЯ ---
def process_section(filename):
    """Обрабатывает данные для одного сечения"""
    pressure = []

    # Загружаем данные из файла
    with open(filename) as file:
        # Читаем показания АЦП и преобразуем в давление
        for line in file:
            try:
                adc_value = int(line.strip())
                p = adc_value / P_k - P_0  # P = k_pressure * N + b_pressure
                pressure.append(p)
            except:
                # Пропускаем пустые строки или нечисловые значения
                pass

    # Создаем массив позиций (от -30 до +30 мм)
    X = [-30 + i * deltr for i in range(len(pressure))]

    # Вычисляем скорость по формуле Бернулли: V = sqrt(2P/ρ)
    # И произведение скорости на радиус (V*r) для графика
    V = [np.sqrt(max(2 * p / ro, 0)) for p in pressure]  # Убедимся, что P >= 0
    Y = [abs(X[i]) * V[i] for i in range(len(V))]

    # Рассчитываем расход Q = 2π * ∫(V(r) * r) dr
    # Используем метод трапеций для численного интегрирования
    consumption = 0
    for i in range(len(V) - 1):
        r1 = abs(X[i]) / 1000  # Переводим мм в метры
        r2 = abs(X[i + 1]) / 1000
        v1 = V[i]
        v2 = V[i + 1]

        # Площадь трапеции: (a + b)/2 * h
        # Здесь: (V(r1)*r1 + V(r2)*r2)/2 * (r2 - r1)
        area = 0.5 * (v1 * r1 + v2 * r2) * (r2 - r1)
        consumption += area

    # Умножаем на 2π и плотность для получения массового расхода (г/с)
    mass_consumption = 2 * np.pi * consumption * ro * 1000  # кг/с -> г/с

    return X, Y, mass_consumption


# --- ОБРАБОТКА ВСЕХ СЕЧЕНИЙ ---
distances = [0, 10, 20, 30, 40, 50, 60, 70]
all_X = []
all_Y = []
all_consumption = []

for distance in distances:
    filename = f"{distance}.csv"
    print(f"Обработка сечения {distance} мм из файла {filename}")

    try:
        X, Y, consumption = process_section(filename)
        all_X.append(X)
        all_Y.append(Y)
        all_consumption.append(consumption)
        print(f"Расход: {consumption:.4f} г/с")
    except Exception as e:
        print(f"Ошибка при обработке файла {filename}: {e}")

# --- ПОСТРОЕНИЕ ГРАФИКА ПРОФИЛЕЙ СКОРОСТИ ---
fig, ax = plt.subplots(figsize=(10, 8))

# Цветовая схема для разных сечений
colors = plt.cm.viridis(np.linspace(0, 1, len(distances)))

for i, distance in enumerate(distances):
    if i < len(all_X) and i < len(all_Y):
        ax.plot(
            all_X[i],
            all_Y[i],
            label=f'{distance} мм: Q = {all_consumption[i]:.2f} г/с',
            color=colors[i],
            linewidth=2
        )

# Настройка графика
ax.minorticks_on()
ax.grid(which='major', linewidth=1, linestyle='-')
ax.grid(which='minor', linestyle=':')

ax.set_xlabel("Положение трубки Пито относительно центра струи X [мм]")
ax.set_ylabel("Произведение скорости струи V и расстояния X [м²/с]")
ax.set_title("График зависимости произведения скорости и расстояния V*X от расстояния X")
ax.set_xlim(-30, 30)  # Устанавливаем разумные пределы по оси X
ax.legend()

plt.tight_layout()
plt.savefig('velocity_profiles.png', dpi=300)
plt.show()

# --- ПОСТРОЕНИЕ ГРАФИКА ЗАВИСИМОСТИ РАСХОДА ---
plt.figure(figsize=(10, 6))
plt.plot(
    distances[:len(all_consumption)],
    all_consumption,
    'o-',
    color='#DB7093',
    linewidth=2,
    markersize=8,
    markerfacecolor='white',
    markeredgewidth=1.5
)

# Добавляем значения расхода на точки
for i, (x, y) in enumerate(zip(distances[:len(all_consumption)], all_consumption)):
    plt.annotate(
        f'{y:.2f}',
        (x, y),
        textcoords="offset points",
        xytext=(0, 10),
        ha='center',
        fontsize=9
    )

# Настройка графика
plt.title('Зависимость расхода от расстояния до сопла', fontsize=16)
plt.xlabel('Расстояние от сопла, мм', fontsize=14)
plt.ylabel('Массовый расход, г/с', fontsize=14)
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.minorticks_on()

plt.tight_layout()
plt.savefig('flow_rate_vs_distance.png', dpi=300)
plt.show()

# --- СОХРАНЕНИЕ РЕЗУЛЬТАТОВ ---
with open("flow_rates.csv", "w") as outfile:
    outfile.write("Расстояние от сопла, мм,Расход, г/с\n")
    for i, distance in enumerate(distances[:len(all_consumption)]):
        outfile.write(f"{distance},{all_consumption[i]:.4f}\n")

print("\nРезультаты сохранены в файл 'flow_rates.csv'")
print("Графики сохранены в файлы 'velocity_profiles.png' и 'flow_rate_vs_distance.png'")