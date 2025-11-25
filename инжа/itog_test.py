from matplotlib import pyplot as plt
import numpy as np

P_k = 97.77
P_0 = 214572.63/P_k

dr = 1
ro = 1.2
deltr = 0.56
count = int(30/deltr)+1
pressure_00 = []
with open("0.csv") as file:
    for line in file:
        p = int(line) / P_k - P_0
        pressure_00.append(p)

X_00 = [(-440 + i*deltr)/18 for i in range(len(pressure_00))]
Y_00 = [(abs(i*deltr)*((1.7*pressure_00[i])**0.5))/160 for i in range(len(pressure_00))]

pressure_10 = []
with open("10.csv") as file:
    for line in file:
        p = int(line) / P_k - P_0
        pressure_10.append(p)

X_10 = [(-420 + i*deltr)/18 for i in range(len(pressure_10))]
Y_10 = [(abs(i*deltr)*((1.7*pressure_10[i])**0.5))/160 for i in range(len(pressure_10))]

pressure_20 = []
with open("20.csv") as file:
    for line in file:
        p = int(line) / P_k - P_0
        pressure_20.append(p)

X_20 = [(-440 + i*deltr)/18 for i in range(len(pressure_20))]
Y_20 = [(abs(i*deltr)*((1.7*pressure_20[i])**0.5))/160 for i in range(len(pressure_20))]

pressure_30 = []
with open("30.csv") as file:
    for line in file:
        p = int(line) / P_k - P_0
        pressure_30.append(p)

X_30 = [(-415 + i*deltr)/18 for i in range(len(pressure_30))]
Y_30 = [(abs(i*deltr)*((1.7*pressure_30[i])**0.5))/160 for i in range(len(pressure_30))]

pressure_40 = []
with open("40.csv") as file:
    for line in file:
        p = int(line) / P_k - P_0
        pressure_40.append(p)

X_40 = [(-435 + i*deltr)/18 for i in range(len(pressure_40))]
Y_40 = [(abs(i*deltr)*((1.7*pressure_40[i])**0.5))/160 for i in range(len(pressure_40))]

pressure_50 = []
with open("50.csv") as file:
    for line in file:
        p = int(line) / P_k - P_0
        pressure_50.append(p)

X_50 = [(-420 + i*deltr)/18 for i in range(len(pressure_50))]
Y_50 = [(abs(i*deltr)*((1.7*pressure_50[i])**0.5))/160 for i in range(len(pressure_50))]

pressure_60 = []
with open("60.csv") as file:
    for line in file:
        p = int(line) / P_k - P_0
        pressure_60.append(p)

X_60 = [(-440 + i*deltr)/18 for i in range(len(pressure_60))]
Y_60 = [(abs(i*deltr)*((1.7*pressure_60[i])**0.5))/160 for i in range(len(pressure_60))]

pressure_70 = []
with open("70.csv") as file:
    for line in file:
        p = int(line) / P_k - P_0
        pressure_70.append(p)

X_70 = [(-410 + i*deltr)/18 for i in range(len(pressure_70))]
Y_70 = [(abs(i*deltr)*((1.7*pressure_70[i])**0.5))/160 for i in range(len(pressure_70))]

fig, ax = plt.subplots(figsize=(8, 10))
ax.plot(X_00, Y_00, label=f'Q (00 мм) = {1.59}[г/с]', color='#FF2E2E')#К
ax.plot(X_10, Y_10, label=f'Q (10 мм) = {1.91}[г/с]', color='#FF952E')#О
ax.plot(X_20, Y_20, label=f'Q (20 мм) = {0.68}[г/с]', color='#FDFF2D')#Ж
ax.plot(X_30, Y_30, label=f'Q (30 мм) = {4.58}[г/с]', color='#2FFF41')#З
ax.plot(X_40, Y_40, label=f'Q (40 мм) = {1.23}[г/с]', color='#369BFF')#Г
ax.plot(X_50, Y_50, label=f'Q (50 мм) = {4.51}[г/с]', color='#3646FF')#С
ax.plot(X_60, Y_60, label=f'Q (60 мм) = {1.61}[г/с]', color='#A138FF')#Ф
ax.plot(X_70, Y_70, label=f'Q (70 мм) = {9.23}[г/с]', color='#FFA4F7')#

ax.minorticks_on()
ax.grid(which='major', linewidth = 1)
ax.grid(which='minor', linestyle = ':')

ax.set_xlabel("Положение трубки Пито относительно центра струи [мм]")
ax.set_ylabel("Скорость воздуха [м/с]")
ax.set_title("Скорость потока воздуха в сечении затопленной струи")

ax.legend()

plt.show()
