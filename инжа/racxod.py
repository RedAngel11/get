import numpy as np
P_k = 96.22261
P_0 = 214572.63/P_k
ro = 1.2
def press(){
    pressure_00 = []
    with open("0.csv") as file:
        for line in file:
            p = int(line) / P_k - P_0
            if p >= 0:
                pressure_00.append(p)
}

def press(i):
    pressures = []
    filename = f"{i}.csv"
    with open(filename) as file:
        for line in file:
            p = int(line.strip()) / P_k - P_0
            if p >= 0:
                pressures.append(p)
    return pressures
consumption_00 = 0
for i in range(100):
    # consumption_00 += 1.2*3.14*0.00045*(abs(-0.024 + i*0.00045)*((1.7*pressure_00[i])**0.5) +
    #                               abs(-0.024 + (i+1)*0.00045)*((1.7*pressure_00[i + 1])**0.5))
    consumption_00 += (2*pressure_00[i]*ro)**0.5*np.pi*(2*abs(X_00[i]*deltr) - deltr**2)