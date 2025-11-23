from matplotlib import pyplot as plt
import numpy as np

Q = []
with open("consumption.txt") as file:
    for line in file:
        c = float(line)
        Q.append(c)

X = [0, 10, 20, 30, 40, 50, 60, 70]

fig, ax = plt.subplots(figsize=(8, 10))
ax.plot(X, Q, label='расход Q (0-70 мм)', color='orange')
ax.scatter(X, Q, color='brown', marker='*')

ax.minorticks_on()
ax.grid(which='major', linewidth = 1)
ax.grid(which='minor', linestyle = ':')

ax.set_xlabel("Расстояние от трубки Пито до сопла")
ax.set_ylabel("Расход [г/с]")
ax.set_title("График зависимости расхода от расстояния до сопла")
ax.legend()
plt.show()