# Obliczane rownianie rozniczkowe: dy/dt = -yt + 3y, y(0) = 1
"""
dy/dt = -yt + 3y, y(0) = 1

Rozwiazanie analityczne:

dy/dt = y(-t + 3)
1/y * dy/dt = (-t + 3)
1/y * dy = (-t + 3) * dt       / calkowanie
ln|y| = (-t^2)/2 + 3t + C_1    / C_1 - stala
y = C_2 * e^((-t^2)/2 + 3t)    / C_2 - stala

1 = C_2 * e^0
C_2 = 1

y = e^((-t^2)/2 + 3t)
"""
import numpy as np
from matplotlib import pyplot as plt


if __name__ == "__main__":
    t0 = 0
    tk = 10
    n = 100

    ask_user = True
    if ask_user:
        print("Podaj czas koncowy tk: ")
        tk = int(input())

    if ask_user:
        print("Podaj liczbe segmentow n: ")
        n = int(input())

    t_arr = np.linspace(start=t0, stop=tk, num=n)
    y_Euler = np.zeros_like(t_arr)
    y_Euler[0] = 1  # Waruenk poczatkowy
    y_Heun = np.copy(y_Euler)
    y_midpoint = np.copy(y_Euler)

    h = 1.0*(tk-t0)/n  # krok czasowy

    # Analitycznie
    y_analitycal = np.exp(-0.5*np.power(t_arr, 2) + 3*t_arr)

    y_prim = lambda y, t: -y*t + 3*y
    # Metoda Eulera
    for i in range(1, y_Euler.shape[0]):
        # y_Euler[i] = y_Euler[i - 1] + (-y_Euler[i - 1] * t_arr[i] + 3 * y_Euler[i - 1]) * h
        y_Euler[i] = y_Euler[i-1] + y_prim(y_Euler[i-1], t_arr[i-1]) * h

    # Metoda Heuna
    for i in range(1, y_Heun.shape[0]):
        slope_1 = y_prim(y_Heun[i-1], t_arr[i-1])

        y_0 = y_Heun[i-1] + slope_1*h
        slope_2 = y_prim(y_0, t_arr[i])

        y_Heun[i] = y_Heun[i-1] + (slope_1+slope_2)/2 * h

    # Metoda Punktu srodkowego
    for i in range(1, y_midpoint.shape[0]):

        y_mid = y_midpoint[i-1] + y_prim(y_midpoint[i-1], t_arr[i-1]) * h/2.0
        slope_mid = y_prim(y_mid, t_arr[i-1]+h/2.0)

        y_midpoint[i] = y_midpoint[i-1] + slope_mid * h

    # Wykresy
    plt.plot(t_arr, y_analitycal)
    plt.plot(t_arr, y_Euler)
    plt.plot(t_arr, y_Heun)
    plt.plot(t_arr, y_midpoint)

    plt.legend(['Analitycznie', 'Metoda Eulera', 'Metoda Heuna', 'Metoda punktu srodkowego'])

    plt.show()

