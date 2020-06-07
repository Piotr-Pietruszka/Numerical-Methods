"""
sinh x, wykresy
"""
import numpy as np
import math
from matplotlib import pyplot as plt
from scipy.special import factorial

def rozw (n, x):

    counter = np.arange(0, n, 1)
    den = np.arange(0, n, 1)

    counter = 2*counter + 1
    den = 2*den + 1

    counter = x**counter
    den = factorial(den)

    elements = counter/den

    return np.sum(elements)

end_point = 2
a = 100 # liczba punktow pomiedzy 0 i 1 (do rysowania wykresu)
x_values = np.arange(0, end_point, 1/a)
y_values = [[], [], []]

for i in range(0, end_point*a):
    y_values[0].append(rozw(1, x_values[i]))
    y_values[1].append(rozw(2, x_values[i]))
    y_values[2].append(rozw(10, x_values[i]))

# Rozwniecia dla n = 10 jest tak bliskie prawdziwej wartości, że się z nią pokrywa na wykresie
# n =1, n = 2, n = 10
plt.plot(x_values, y_values[0])
plt.plot(x_values, y_values[1])
plt.plot(x_values, y_values[2])

y_true = np.sinh(x_values)
plt.plot(x_values, y_true)
plt.legend(["n=1", "n=2", "n=10", "true"])

plt.show()

