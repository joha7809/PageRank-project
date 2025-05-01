from sympy import *
import matplotlib.pyplot as plt
import numpy as np
init_printing()

#Matrix defineres
A = Matrix([[0.0005,0.9995],[0.9995,0.0005]])

#Undersøger om matrix er diagonaliserbar. Det er den, hvis funktionen kører
A.diagonalize()

#Sandsynlighedsvektor
B = Matrix([0.6, 0.4])

vectors = []
raisedTo = [1,2,5,10,25,1000]

Md = (1-0.85)/2*Matrix([[1,1],[1,1]])+0.85*A


for i in range(len(raisedTo)):
    vectors.append(A**raisedTo[i])

x_vals = [float(vec[0]) for vec in vectors]
y_vals = [float(vec[1]) for vec in vectors]

colorsG = ["pink", "green", "red", "orange", "yellow", "black", "blue", "lime"]

plt.figure(figsize=(8, 6))
i = 0
for x, y in zip(x_vals, y_vals):
    plt.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1, color=colorsG[i], label=f'Matrix løftet i ^{raisedTo[i]}')
    i += 1

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Plot of Transformed Vectors')
plt.grid(True)
plt.xlim(min(0, max(x_vals)+0.1))
plt.ylim(min(0, max(y_vals)+0.1))
plt.legend(loc='lower right') #Viser menu
plt.show()