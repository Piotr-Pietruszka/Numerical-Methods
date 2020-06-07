"""
dx/dt = -10x  +10y
dy/dt = 28x - y - xz
dz/dt = -8/3z + xy

t0 = 0
tk = 25
h = 0.03125
x(0) = y(0) = z(0)
"""

import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


f1 = lambda x, y: -10.0*x + 10.0*y
f2 = lambda x, y, z: 28.0*x - y - x*z
f3 = lambda x, y, z: -8.0/3.0*z + x*y
rk_func = lambda k1, k2, k3, k4, var, h: var + 1.0/6.0 * (k1 + 2*k2 + 2*k3 + k4) * h

t_0 = 0.0
t_k = 25.0

h = 0.03125

x_0, y_0, z_0 = 5.0, 5.0, 5.0


def rk_step(x, y, z, h):
    """
    1 krok metody Rungego-Kutty czwartego rzedu
    :param x: wartosc zmiennej x, w danej chwili czasu
    :param y: wartosc zmiennej y, w danej chwili czasu
    :param z: wartosc zmiennej z, w danej chwili czasu
    :param h: krok czasowy
    :return: wartosci x, y, z w nastepnej chwili czasu
    """
    k1 = f1(x, y), f2(x, y, z), f3(x, y, z)  # t=0h

    x_1, y_1, z_1 = x + k1[0]*h/2.0, y + k1[1]*h/2.0, z + k1[2]*h/2.0
    k2 = f1(x_1, y_1), f2(x_1, y_1, z_1), f3(x_1, y_1, z_1)  # t=0.5h

    x_2, y_2, z_2 = x + k2[0]*h/2.0, y + k2[1] * h/2.0, z + k2[2]*h/2.0
    k3 = f1(x_2, y_2), f2(x_2, y_2, z_2), f3(x_2, y_2, z_2)   # t=0.5h

    x_3, y_3, z_3 = x + k3[0]*h, y + k3[1]*h, z + k3[2]*h
    k4 = f1(x_3, y_3), f2(x_3, y_3, z_3), f3(x_3, y_3, z_3)   # t=1h
    x_new = rk_func(k1[0], k2[0], k3[0], k4[0], x, h)
    y_new = rk_func(k1[1], k2[1], k3[1], k4[1], y, h)
    z_new = rk_func(k1[2], k2[2], k3[2], k4[2], z, h)

    return x_new, y_new, z_new


time_ar = np.arange(t_0, t_k, h)  # Tablica wartosci czasu

x_ar, y_ar, z_ar = np.zeros_like(time_ar), np.zeros_like(time_ar), np.zeros_like(time_ar)
x_ar[0], y_ar[0], z_ar[0] = x_0, y_0, z_0  # Warunki poczatkowe

# Petla po czasie
for i in range(time_ar.shape[0]-1):
    x_ar[i+1], y_ar[i+1], z_ar[i+1] = rk_step(x_ar[i], y_ar[i], z_ar[i], h)


# Wykresy - oddzielnie przebiegi x(t), y(t) i z(t) oraz trajektoria fazowa (3d)
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()
fig3, ax3 = plt.subplots()

ax1.plot(time_ar, x_ar)


fig1.suptitle('x(t)')

ax2.plot(time_ar, y_ar)
fig2.suptitle('y(t)')

ax3.plot(time_ar, z_ar)
fig3.suptitle('z(t)')

fig_3d = plt.figure()
ax_3d = plt.axes(projection='3d')

ax_3d.plot3D(x_ar, y_ar, z_ar)
ax_3d.set_xlabel('x')
ax_3d.set_ylabel('y')
ax_3d.set_zlabel('z')

plt.show()
