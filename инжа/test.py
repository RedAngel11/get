from matplotlib import pyplot as plt
import numpy as np

P_k = 96.22261
P_0 = 214572.63/P_k  #1189
# S_k = 184
# S_0 = 0

dr = 1

ro = 1.2
deltr = 0.45
count = int(30/deltr)+1
pressure_00 = []
with open("0.csv") as file:
    for line in file:
        p = int(line) / P_k - P_0
        if p >= 0:
            pressure_00.append(p)

# print(pressure_00)
X_00 = [-30 + i*deltr for i in range(len(pressure_00))]
Y_00 = [abs(-30 + i*deltr)*((1.7*pressure_00[i])**0.5) for i in range(len(pressure_00))]

consumption_00 = 0
for i in range(count):
    # consumption_00 += 1.2*3.14*0.00045*(abs(-0.024 + i*0.00045)*((1.7*pressure_00[i])**0.5) +
    #                               abs(-0.024 + (i+1)*0.00045)*((1.7*pressure_00[i + 1])**0.5))
    consumption_00 += (2*pressure_00[i]*ro)**0.5*np.pi*(2*abs(X_00[i]*deltr) - deltr**2)

pressure_10 = []
with open("10.csv") as file:
    for line in file:
        p = int(line) / P_k - P_0
        if p >= 0:
            pressure_10.append(p)
# print(pressure_10)
# pressure_10.pop(0)
X_10 = [-30 + i*deltr for i in range(len(pressure_10))]
Y_10 = [abs(-30 + i*deltr)*((1.7*pressure_10[i])**0.5) for i in range(len(pressure_10))]

consumption_10 = 0
for i in range(count):
    # consumption_10 += p*np.pi*dr*(i*dr*((1.7*pressure_10[i])**0.5) +
    #                               (i + 1)*dr*((1.7*pressure_10[i + 1])**0.5))
    consumption_10 += (2*pressure_10[i]*ro)**0.5*np.pi*(2*abs(X_10[i]*deltr) - deltr**2)

pressure_20 = []
with open("20.csv") as file:
    for line in file:
        p = int(line) / P_k - P_0
        if p >= 0:
            pressure_20.append(p)

X_20 = [-30 + i*deltr for i in range(len(pressure_20))]
Y_20 = [abs(-30 + i*deltr)*((1.7*pressure_20[i])**0.5) for i in range(len(pressure_20))]

consumption_20 = 0
for i in range(count):
    # consumption_20 += p*np.pi*dr*(i*dr*((1.7*pressure_20[i])**0.5) +
    #                               (i + 1)*dr*((1.7*pressure_20[i + 1])**0.5))
    consumption_20 += (2*pressure_20[i]*ro)**0.5*np.pi*(2*abs(X_20[i]*deltr) - deltr**2)

pressure_30 = []
with open("30.csv") as file:
    for line in file:
        p = int(line) / P_k - P_0
        if p >= 0:
            pressure_30.append(p)
# pressure_30.pop(0)
X_30 = [-30 + i*deltr for i in range(len(pressure_30))]
Y_30 = [abs(-30 + i*deltr)*((1.7*pressure_30[i])**0.5) for i in range(len(pressure_30))]

consumption_30 = 0
for i in range(count):
    # consumption_30 += p*np.pi*dr*(i*dr*((1.7*pressure_30[i])**0.5) +
    #                               (i + 1)*dr*((1.7*pressure_30[i + 1])**0.5))
    consumption_30 += (2*pressure_30[i]*ro)**0.5*np.pi*(2*abs(X_30[i]*deltr) - deltr**2)

pressure_40 = []
with open("40.csv") as file:
    for line in file:
        p = int(line) / P_k - P_0
        if p >= 0:
            pressure_40.append(p)
# pressure_40.pop(0)
X_40 = [-30 + i*deltr for i in range(len(pressure_40))]
Y_40 = [abs(-30 + i*deltr)*((1.7*pressure_40[i])**0.5) for i in range(len(pressure_40))]

consumption_40 = 0
for i in range(count):
    # consumption_40 += p*np.pi*dr*(i*dr*((1.7*pressure_40[i])**0.5) +
    #                               (i + 1)*dr*((1.7*pressure_40[i + 1])**0.5))
    consumption_40 += (2*pressure_40[i]*ro)**0.5*np.pi*(2*abs(X_40[i]*deltr) - deltr**2)

pressure_50 = []
with open("50.csv") as file:
    for line in file:
        p = int(line) / P_k - P_0
        if p >= 0:
            pressure_50.append(p)

X_50 = [-30 + i*deltr for i in range(len(pressure_50))]
Y_50 = [abs(-30 + i*deltr)*((1.7*pressure_50[i])**0.5) for i in range(len(pressure_50))]

consumption_50 = 0
for i in range(count):
    # consumption_50 += p*np.pi*dr*(i*dr*((1.7*pressure_50[i])**0.5) +
    #                               (i + 1)*dr*((1.7*pressure_50[i + 1])**0.5))
    consumption_50 += (2*pressure_50[i]*ro)**0.5*np.pi*(2*abs(X_50[i]*deltr) - deltr**2)

pressure_60 = []
with open("60.csv") as file:
    for line in file:
        p = int(line) / P_k - P_0
        if p >= 0:
            pressure_60.append(p)

X_60 = [-30 + i*deltr for i in range(len(pressure_60))]
Y_60 = [abs(-30 + i*deltr)*((1.7*pressure_60[i])**0.5) for i in range(len(pressure_60))]

consumption_60 = 0
for i in range(count):
    # consumption_60 += p*np.pi*dr*(i*dr*((1.7*pressure_60[i])**0.5) +
    #                               (i + 1)*dr*((1.7*pressure_60[i + 1])**0.5))
    consumption_60 += (2*pressure_60[i]*ro)**0.5*np.pi*(2*abs(X_60[i]*deltr) - deltr**2)

pressure_70 = []
with open("70.csv") as file:
    for line in file:
        p = int(line) / P_k - P_0
        if p >= 0:
            pressure_70.append(p)

X_70 = [-30 + i*deltr for i in range(len(pressure_70))]
Y_70 = [abs(-30 + i*deltr)*((1.7*pressure_70[i])**0.5) for i in range(len(pressure_70))]

consumption_70 = 0
for i in range(count):
    consumption_70 += (2*pressure_70[i]*ro)**0.5*np.pi*(2*abs(X_70[i]*deltr) - deltr**2)

fig, ax = plt.subplots(figsize=(8, 10))
ax.plot(X_00, Y_00, label='00 мм', color='red')
ax.plot(X_10, Y_10, label='10 мм', color='orange')
ax.plot(X_20, Y_20, label='20 мм', color='yellow')
ax.plot(X_30, Y_30, label='30 мм', color='green')
ax.plot(X_40, Y_40, label='40 мм', color='blue')
ax.plot(X_50, Y_50, label='50 мм', color='purple')
ax.plot(X_60, Y_60, label='60 мм', color='brown')
ax.plot(X_70, Y_70, label='70 мм', color='pink')

ax.minorticks_on()
ax.grid(which='major', linewidth = 1)
ax.grid(which='minor', linestyle = ':')

ax.set_xlabel("Положение трубки Пито относительно центра струи X [мм]")
ax.set_ylabel("Произведение скорости струи V и расстояния X")
ax.set_title("График зависимости произведения скорости и расстояния V*X от расстояния X")
ax.legend()
plt.show()

consumption = [consumption_00, consumption_10, consumption_20, consumption_30, consumption_40, consumption_50, consumption_60, consumption_70]
consumptionStr = [str(item/10000) for item in consumption]
with open("consumption.txt", "w") as outfile:
    outfile.write("\n".join(consumptionStr))

print(pressure_00, pressure_10, pressure_20, pressure_30, pressure_40, pressure_50, pressure_60, pressure_70, sep='\n')