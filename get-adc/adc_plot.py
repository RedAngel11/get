import matplotlib.pyplot as plt

def plot_voltage_vs_time(time, voltage, max_voltage):

    plt.figure(figsize=(10, 6))
    plt.plot(time, voltage, color ="green", linewidth=1.5)
    
    # Оформление
    plt.title("График зависимости напряжения на входе АЦП от времени", fontsize=14)
    plt.xlabel("Время, с", fontsize=10)
    plt.ylabel("Напряжение, В", fontsize=10)
    
    plt.xlim(0, 3)# тут сделать коряво! возможно стоит когда-то поменять
    plt.ylim(0, 3.5)
    
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    
    plt.tight_layout()  # Чтобы всё красиво вмещалось
    plt.show()

def plot_sampling_period_hist(time_values):

    if len(time_values) < 2:
        print("Недостаточно данных для гистограммы.")
        return
    
    # Вычисляем разницу между соседними временами → периоды измерений
    sampling_periods = []
    for i in range(1, len(time_values)):
        period = time_values[i] - time_values[i-1]
        sampling_periods.append(period)
    
    plt.figure(figsize=(10, 6))
    plt.hist(sampling_periods, bins=25, range=(min(sampling_periods), max(sampling_periods)), color='red', edgecolor='black', alpha=0.7)
    
    plt.title("Распределение периодов дискретизации измерений\nпо времени на одно измерение", fontsize=12)
    plt.xlabel("Период измерения, с", fontsize=10)
    plt.ylabel("Количество измерений", fontsize=10)
    

    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()