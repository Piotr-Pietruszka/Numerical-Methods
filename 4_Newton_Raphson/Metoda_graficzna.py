"""
y =  -x**2 - x + 3
y = x**2 + x*y



y = -x**2 - x +3
y = (x**2)/(1-x)

Metoda graficzna

# Układ ma 3 rozwiazania (metoda graficzna, więc w przyblliżeniu):
# x = -1.9, y = 1.25
# x = 0.7, y = 1.75
# x = 2.2, y = -4

"""

import numpy as np
from matplotlib import pyplot as plt




x_1 = np.arange(-5+0.05, 5, 0.1)
x_2 = np.arange(-5+0.05, 5, 0.1)

y_1 = -x_1**2 - x_1 + 3
y_2 = (x_2**2)/(1-x_2)

plt.plot(x_1, y_1, color='blue')
plt.plot(x_2, y_2, color='red')

plt.grid()
plt.legend(["y =  -x**2 - x + 3", "y = (x**2)/(1-x)"])
plt.show()

