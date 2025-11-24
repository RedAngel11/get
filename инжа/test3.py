from matplotlib import pyplot as plt
import numpy as np

P_k = 96.22261
P_0 = 214572.63/P_k  #1189
# S_k = 184
# S_0 = 0

dr = 1

ro = 1.2
deltr = 0.56

count = int(24/deltr)+1
pressure_00 = []
with open("0.csv") as file:
    for line in file:
        p = int(line) / P_k - P_0

        pressure_00.append(p)

# print(pressure_00)
X_00 = [-24 + i*deltr for i in range(len(pressure_00))]
Y_00 = [abs(-24 + i*deltr)*((1.7*pressure_00[i])**0.5) for i in range(len(pressure_00))]


pressure_10 = []
with open("10.csv") as file:
    for line in file:
        p = int(line) / P_k - P_0

        pressure_10.append(p)
# print(pressure_10)
# pressure_10.pop(0)
X_10 = [-24 + i*deltr for i in range(len(pressure_10))]
Y_10 = [abs(-24 + i*deltr)*((1.7*pressure_10[i])**0.5) for i in range(len(pressure_10))]


pressure_20 = []
with open("20.csv") as file:
    for line in file:
        p = int(line) / P_k - P_0

        pressure_20.append(p)

X_20 = [-24 + i*deltr for i in range(len(pressure_20))]
Y_20 = [abs(-24 + i*deltr)*((1.7*pressure_20[i])**0.5) for i in range(len(pressure_20))]


pressure_30 = []
with open("30.csv") as file:
    for line in file:
        p = int(line) / P_k - P_0

        pressure_30.append(p)
# pressure_30.pop(0)
X_30 = [-24 + i*deltr for i in range(len(pressure_30))]
Y_30 = [abs(-24 + i*deltr)*((1.7*pressure_30[i])**0.5) for i in range(len(pressure_30))]


pressure_40 = []
with open("40.csv") as file:
    for line in file:
        p = int(line) / P_k - P_0

        pressure_40.append(p)
# pressure_40.pop(0)
X_40 = [-24 + i*deltr for i in range(len(pressure_40))]
Y_40 = [abs(-24 + i*deltr)*((1.7*pressure_40[i])**0.5) for i in range(len(pressure_40))]


pressure_50 = []
with open("50.csv") as file:
    for line in file:
        p = int(line) / P_k - P_0

        pressure_50.append(p)

X_50 = [-24 + i*deltr for i in range(len(pressure_50))]
Y_50 = [abs(-24 + i*deltr)*((1.7*pressure_50[i])**0.5) for i in range(len(pressure_50))]

pressure_60 = []
with open("60.csv") as file:
    for line in file:
        p = int(line) / P_k - P_0

        pressure_60.append(p)

X_60 = [-24 + i*deltr for i in range(len(pressure_60))]
Y_60 = [abs(-24 + i*deltr)*((1.7*pressure_60[i])**0.5) for i in range(len(pressure_60))]


pressure_70 = []
with open("70.csv") as file:
    for line in file:
        p = int(line) / P_k - P_0

        pressure_70.append(p)

X_70 = [-24 + i*deltr for i in range(len(pressure_70))]
Y_70 = [abs(-24 + i*deltr)*((1.7*pressure_70[i])**0.5) for i in range(len(pressure_70))]

consumption = []
with open("consumption.txt") as cons:
    for i in cons:
        consumption.append(round(float(i.strip()), 2))

fig, ax = plt.subplots(figsize=(8, 10))
ax.plot(X_00, Y_00, label=f'Q (00 мм) = {consumption[0]} [г/с]', color='red')
ax.plot(X_10, Y_10, label=f'Q (10 мм) = {consumption[1]}[г/с]', color='orange')
ax.plot(X_20, Y_20, label=f'Q (20 мм) = {consumption[2]}[г/с]', color='yellow')
ax.plot(X_30, Y_30, label=f'Q (30 мм) = {consumption[3]}[г/с]', color='green')
ax.plot(X_40, Y_40, label=f'Q (40 мм) = {consumption[4]}[г/с]', color='blue')
ax.plot(X_50, Y_50, label=f'Q (50 мм) = {consumption[5]}[г/с]', color='purple')
ax.plot(X_60, Y_60, label=f'Q (60 мм) = {consumption[6]}[г/с]', color='brown')
ax.plot(X_70, Y_70, label=f'Q (70 мм) = {consumption[7]}[г/с]', color='pink')



ax.minorticks_on()
ax.grid(which='major', linewidth = 1)
ax.grid(which='minor', linestyle = ':')

ax.set_xlabel("Положение трубки Пито относительно центра струи [мм]")
ax.set_ylabel("Скорость воздуха [м/с]")
ax.set_title("Скорость потока воздуха в сечении затопленной струи")

ax.set_xlim([-30, 30])
ax.set_ylim([-1, 35])

ax.legend()

plt.show()