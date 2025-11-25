import numpy as np

P_k = 96.22261
P_0 = 214572.63 / P_k
ro = 1.2  # Плотность воздуха (кг/м³)
deltr_mm = 0.056

def press(i):
    """
    Загружает показания АЦП из файла и преобразует в давление.
    """
    filename = f"{i * 10}.csv"
    pressures = []

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            adc_value = int(line)
            p = adc_value / P_k - P_0
            if p >= 0:
                pressures.append(p)
    return pressures

def calculate_consumption(X_mm, pressure):
    """
    Рассчитывает массовый расход методом трапеций
    """
    if len(pressure) == 0 or len(X_mm) < 2:
        return 0.0

    # Вычисляем скорость по формуле Бернулли: V = sqrt(2P/ρ)
    V = [np.sqrt(2 * p / ro) for p in pressure]

    # Преобразуем X из мм в м (КРИТИЧЕСКИ ВАЖНО!)
    X_m = np.array(X_mm) / 1000  # мм → м

    # Находим центр струи по максимуму скорости
    max_idx = np.argmax(V)
    center = X_m[max_idx]

    # Центрируем координаты относительно центра струи
    centered_X_m = X_m - center

    # Оставляем только точки с r >= 0 (правая половина)
    mask = centered_X_m >= 0
    r_positive = centered_X_m[mask]
    V_positive = np.array(V)[mask]

    if len(r_positive) < 2:
        return 0.0

    # Формула: ∑ 0.5*(V_i*r_i + V_{i+1}*r_{i+1}) * (r_{i+1} - r_i)
    integral = 0.0
    for i in range(len(r_positive) - 1):
        r_i = r_positive[i]
        r_next = r_positive[i + 1]
        V_i = V_positive[i]
        V_next = V_positive[i + 1]

        # Площадь трапеции под кривой V(r)*r
        area = 0.5 * (V_i * r_i + V_next * r_next) * (r_next - r_i)
        integral += area

    # Объёмный расход: Q_vol = 2π × интеграл
    volume_flow_rate = 2 * np.pi * integral  # м³/с

    # Массовый расход: Q_mass = ρ × Q_vol
    mass_flow_rate_g_s = volume_flow_rate * ro * 1000  # кг/с → г/с

    return mass_flow_rate_g_s

all_consumptions = []

for i in range(8):
    distance = i * 10
    pressure_data = press(i)

    # Создаём массив позиций: от начальной позиции с шагом deltr_mm
    # Предполагаем, что измерения проводились от -50 до +50 мм (радиус 50 мм)
    num_points = len(pressure_data)
    start_pos = -50.0  # Начальная позиция
    positions = [start_pos + idx * deltr_mm for idx in range(num_points)]

    # Рассчитываем расход
    consumption = calculate_consumption(positions, pressure_data)
    all_consumptions.append(consumption)

print("РЕЗУЛЬТАТЫ РАСХОДА ПО СЕЧЕНИЯМ:")

for i, q in enumerate(all_consumptions):
    print(f"Q({i * 10:2d} мм) = {q:8.4f} г/с")

print("\nСписок расходов:")
print([f"{q:.4f}" for q in all_consumptions])
