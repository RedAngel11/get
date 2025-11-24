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

ax.set_xlabel("Расстояние от трубки Пито до сопла")
ax.set_ylabel("Расход [г/с]")
ax.set_title("График зависимости расхода от расстояния до сопла")
ax.legend()
plt.show()