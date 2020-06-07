import numpy as np
from numpy import transpose as tr
from matplotlib import pyplot as plt

# Wczytanie danych z pliku
file = open("measurements.txt", 'r')
lines = file.readlines()

meas_x, meas_y = [], []
for line in lines:
    px, py = line.split()
    meas_x.append(float(px))
    meas_y.append(float(py))

file.close()

meas_y = np.array(meas_y)
meas_x = np.array(meas_x)

T = 1
s = tr(np.array([meas_x[0], meas_y[0], 0, 0]))
F = np.array([[1, 0, T, 0],
              [0, 1, 0, T],
              [0, 0, 1, 0],
              [0, 0, 0, 1]])

G = tr(np.array([[0, 0, 1, 0],
                 [0, 0, 0, 1]]))

H = np.array([[1, 0, 0, 0],
              [0, 1, 0, 0]])
P = 5.0*np.eye(4, 4)
Q = 0.25*np.eye(2, 2)
R = 2.0*np.eye(2, 2)


x_kal = []
y_kal = []

x_kal.append(s[0])
y_kal.append(s[1])
for i in range(1, len(meas_x)):
    # Faza predykcji
    # ------------------------------
    # Szacowanie stanu na podstawie poprzedniego
    s_pred = F @ s

    # Uaktualnieni macierzy kowariancji
    P = F @ P @ tr(F) + G @ Q @ tr(G)

    # Przewidywany pomiar
    z_pred = H @ s_pred
    # ------------------------------

    # Pomiar wlasciwy
    z = np.array([meas_x[i], meas_y[i]])

    # Innowacja
    e = z - z_pred

    # Macierz kowariancji innowacji
    S = H @ P @ tr(H) + R

    # Wzmocnienie Kalmana
    K = P @ tr(H) @  np.linalg.inv(S)

    # Nowa estymata stanu
    s = s_pred + K @ e

    # Aktualizzacja 2 macierzy kowariancji
    P = (np.eye(K.shape[0], K.shape[0]) - K @ H) @ P

    x_kal.append(s[0])
    y_kal.append(s[1])


x_pred = []
y_pred = []
x_pred.append(s[0])
y_pred.append(s[1])
for i in range(5):
    # Wyznaczanie kolejnych 5 probek - bez pomiaru
    # Jedyni szacowanie stanu na podstawie poprzedniego
    s_pred = F @ s

    # Nowa estymata stanu
    s = s_pred

    x_pred.append(s[0])
    y_pred.append(s[1])

plt.plot(meas_x, meas_y, 'x')
plt.plot(x_kal, y_kal)
plt.plot(x_pred, y_pred, '--')
plt.plot(x_pred[-1], y_pred[-1], 'o')

plt.show()
