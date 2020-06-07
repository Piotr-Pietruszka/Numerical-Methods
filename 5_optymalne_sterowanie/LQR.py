"""
Zwiększanie c1 względem c2 oznacza przypisanie stanowi większej wagi w wyznaczaniu błędu.
Powoduje to zmniejszenie wartości sygnału wyjściowego w stanie ustalonym i przybliżenie jej
do wartości zadanej. Oznacza też jednak krótkotwały, ale gwałtowny wzrost wartości bezwzględnej
sygnału sterującego.

Zwiększanie c2 wygładza wykres (brak gwałtownych zmian), ale zmniejsza dokładność (większe
wartości ustalone sygnałów).

"""
import numpy as np
from numpy import transpose as tr
from numpy import invert as inv
from matplotlib import pyplot as plt

def ricatti(A, B, Q, R, P):
    n_r = 80
    for i in range(n_r):
        P = Q + tr(A) @ (P - P@B @ ((R+tr(B)@P@B)**(-1.0)) @ tr(B)@P) @ A
    return P

# Model stanowy
A = np.array([[2.85, -1.85, 0.3],
              [1,     0,    0],
              [0,     1,    0]])

B = np.array([[1], [0], [0]])

C = np.array([1, 1, 1])

U = 1

X = np.array([[0], [0], [0]])
Y_t = []

# Koszt
c1 = 900
Q = c1*np.array([[1, 0, 0],
                 [0, 1, 0],
                 [0, 0, 1]])
c2 = 100
R = c2

# Sprzezenie
F = np.array([[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]])
P = np.array([[1, 0, 0],
              [0, 1, 0],
              [0, 0, 1]])
P = ricatti(A, B, Q, R, P)
F = ((R + tr(B) @ P @ B) ** (-1.0)) @ tr(B) @ P @ A


n = 100
U_t = []
for t in range(n):
    U = 1 - (F@X)[0, 0]
    Y = C @ X
    X = A @ X + B * U

    Y_t.append(Y[0])
    U_t.append(U)

Y_t_x = np.arange(len(Y_t))

plt.plot(Y_t_x, Y_t)
plt.plot(Y_t_x, U_t)
plt.legend(('y', 'u'))
plt.show()

