"""
Brak sprzezenia od stanu - uklad jest niestabilny

"""
import numpy as np
from matplotlib import pyplot as plt


# Model stanowy
A = np.array([[2.85, -1.85, 0.3],
              [1,     0,    0],
              [0,     1,    0]])

B = np.array([[1], [0], [0]])

C = np.array([1, 1, 1])

D = 0


U = 1
X = np.array([[0], [0], [0]])
Y_t = []

n = 100

for t in range(n):
    X = A @ X + B * U
    Y = C @ X
    Y_t.append(Y[0])


Y_t_x = np.arange(len(Y_t))
plt.plot(Y_t_x, Y_t)
plt.show()

