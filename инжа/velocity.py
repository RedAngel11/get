from matplotlib import pyplot as plt

P_k = 4.36
P_0 = 1589.756/P_k  #1189

pressure_00 = []

with open("data\\00 mm.txt") as file:
    _ = file.readline()
    _ = file.readline()
    _ = file.readline()
    for line in file:
        p = int(line) / P_k - P_0
        pressure_00.append(p)

X_00 = [-24 + i*0.45 for i in range(len(pressure_00))]
Y_00 = [(1.7*pressure_00[i])**0.5 for i in range(len(pressure_00))]

pressure_10 = []
with open("data\\10 mm.txt") as file:
    _ = file.readline()
    _ = file.readline()
    _ = file.readline()
    for line in file:
        p = int(line) / P_k - P_0
        pressure_10.append(p)

pressure_10.pop(0)
X_10 = [-24 + i*0.45 for i in range(len(pressure_10))]
Y_10 = [(1.7*pressure_10[i])**0.5 for i in range(len(pressure_10))]

pressure_20 = []
with open("data\\20 mm.txt") as file:
    _ = file.readline()
    _ = file.readline()
    _ = file.readline()
    for line in file:
        p = int(line) / P_k - P_0
        pressure_20.append(p)

X_20 = [-24 + i*0.45 for i in range(len(pressure_20))]
Y_20 = [(1.7*pressure_20[i])**0.5 for i in range(len(pressure_20))]

pressure_30 = []
with open("data\\30 mm.txt") as file:
    _ = file.readline()
    _ = file.readline()
    _ = file.readline()
    for line in file:
        p = int(line) / P_k - P_0
        pressure_30.append(p)
pressure_30.pop(0)
X_30 = [-24 + i*0.45 for i in range(len(pressure_30))]
Y_30 = [(1.7*pressure_30[i])**0.5 for i in range(len(pressure_30))]

pressure_40 = []
with open("data\\40 mm.txt") as file:
    _ = file.readline()
    _ = file.readline()
    _ = file.readline()
    for line in file:
        p = int(line) / P_k - P_0
        pressure_40.append(p)
pressure_40.pop(0)
X_40 = [-24 + i*0.45 for i in range(len(pressure_40))]
Y_40 = [(1.7*pressure_40[i])**0.5 for i in range(len(pressure_40))]

pressure_50 = []
with open("data\\50 mm.txt") as file:
    _ = file.readline()
    _ = file.readline()
    _ = file.readline()
    for line in file:
        p = int(line) / P_k - P_0
        pressure_50.append(p)

X_50 = [-24 + i*0.45 for i in range(len(pressure_50))]
Y_50 = [(1.7*pressure_50[i])**0.5 for i in range(len(pressure_50))]

pressure_60 = []
with open("data\\60 mm.txt") as file:
    _ = file.readline()
    _ = file.readline()
    _ = file.readline()
    for line in file:
        p = int(line) / P_k - P_0
        pressure_60.append(p)

X_60 = [-24 + i*0.45 for i in range(len(pressure_60))]
Y_60 = [(1.7*pressure_60[i])**0.5 for i in range(len(pressure_60))]

pressure_70 = []
with open("data\\70 mm.txt") as file:
    _ = file.readline()
    _ = file.readline()
    _ = file.readline()
    for line in file:
        p = int(line) / P_k - P_0
        pressure_70.append(p)

X_70 = [-24 + i*0.45 for i in range(len(pressure_70))]
Y_70 = [(1.7*pressure_70[i])**0.5 for i in range(len(pressure_70))]

consumption = []
with open("consumption.txt") as cons:
    for i in cons:
        consumption.append(round(float(i), 2))
fig, ax = plt.subplots()
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