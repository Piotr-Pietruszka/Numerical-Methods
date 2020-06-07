"""
Metoda iteracyjna: zbiega się tylko do jednego rozwiązania:

x:2.198691243502455
y:-4.03293442797216

Punkt startowy:
x_it = 3
y_it = -7

Niezbieżna (oscylacje)
Punkt startowy:
x_it = 1.16
y_it = -7

Zmiana punktu startowego doprowadza jedynie do utracenia zbieżności
i nie pomaga w odnalezieniu pozostałych rozwiązań.



Metoda Newtona-Raphsona:
W zależności od punktu startowego zbiega się do wszystich rozwiązań:

x:-1.9122291784843966
y:1.2556087474372863
Start:
x = 0
y = -2

x:2.1986912435159973
y:-4.032934427829919
Start:
x = 3
y = -7

x:0.7135379349683996
y:1.7773256803926323
Start:
x = 0
y = 7



Metoda Newtona-Raphson zbiega się na ogół szybciej, co można zaobserowować  na wykresie dla
punku startowego (3, -7).

Jako błąd przyjąłem zmianę odległości szacowanego rozwiązania od rozwiązania
poprzedniego w stosunku do odległości obecnego rozwiązania od początku układu
współrzędnych.
"""

import numpy as np
from matplotlib import pyplot as plt
import math

# y = -x**2 - x +3
# y = (x**2)/(1-x) <=> x = 1 - x**2 / y
n = 1000

# Iteracyjen podstawianie:
# ------------------------
# Zbiezna do punktu x=2.2, y=-4 z: x=3, y=-7
# Zbieznosc: 1.17, -7, nie zbieżność: 1.165, -7

# Start
x_it = 3
y_it = -7


x_prev_it = x_it
y_prev_it = y_it
err_it = 100
err_it_list = []
acc_it = 1e-8
# ------------------------

# Newton-Raphson
# ------------------------
# start x = 0, y = -2 - rozw: x=1.25, y=-1.9
# start x = 3, y = -7 - rozw: x=2.2, y=-4
# start x = 0, y = 7 - rozw: x=0.7, y=1.75
df1_dy = 1

# Start
x_start = 3
y_start = -7

x = x_start
y = y_start

x_prev = x
y_prev = y
err_n = 100
err_n_list = []
acc_n = 1e-8
# ------------------------

for i in range(n):

    # Iteracyjne podstawianie
    y_it = -x_it**2 - x_it + 3
    x_it = 1 - x_it ** 2 / y_it

    # x_it = math.sqrt(-x_it - y_it + 3)
    # y_it = x_it ** 2 + x_it * y_it

    err_it = math.sqrt(((x_it - x_prev_it) ** 2 + (y_it - y_prev_it) ** 2) / (x_it ** 2 + y_it ** 2)) * 100
    err_it_list.append(err_it)

    x_prev_it = x_it
    y_prev_it = y_it

    # Newton-Raphson
    f1 = x ** 2 + x + y - 3
    f2 = y - x ** 2 - x * y

    df1_dx = 2 * x + 1

    df2_dx = -2 * x - y
    df2_dy = 1 - x

    x = x - (f1 * df2_dy - f2 * df1_dy) / (df1_dx * df2_dy - df1_dy * df2_dx)
    y = y - (f2 * df1_dx - f1 * df2_dx) / (df1_dx * df2_dy - df1_dy * df2_dx)

    err_n = math.sqrt( ((x-x_prev)**2 + (y - y_prev)**2) / (x**2 + y**2) ) * 100
    err_n_list.append(err_n)

    x_prev = x
    y_prev = y

    if err_n < acc_n and err_it < acc_it:
        break
        
print(f"x_start:{x_start}")
print(f"y_start:{y_start}")
print("\n")

print(f"x_it:{x_it}")
print(f"y_it:{y_it}")
print("\n")

print(f"x_NR:{x}")
print(f"y_NR:{y}")
print("\n")

err_plt_x_it = np.arange(0, len(err_it_list))
err_plt_x_n = np.arange(0, len(err_n_list))

plt.plot(err_plt_x_it, err_it_list)
plt.plot(err_plt_x_n, err_n_list)
plt.legend(('Blad iteracyjna', 'Blad Newtona'))
plt.show()


