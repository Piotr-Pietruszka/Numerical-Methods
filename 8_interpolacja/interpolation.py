import numpy as np
from matplotlib import pyplot as plt

np.set_printoptions(linewidth=300)


def my_polynomial(x, A):
    """
    Wielomian o wspolczynnikach A - do interpolacji wielomianem Newtona
    :param x: wartosc na osi x
    :param A: wspolczynniki wielomianu w kolejnosci od najwyzszych poteg
    :return: wartosc wielomianu dla podanego x
    """
    result = 0
    for i in range(A.shape[0]):
        result += A[i] * x ** (A.shape[0] - i - 1)
    return result


def spline(x_spl, x_points, A, B, C, D):
    """
    Obliczanie wartosci interpolowanych - funkcje sklejane
    :param x_spl: dziedzina
    :param x_points: punkty pomiedzy ktorymi jest realizowana interpolacja
    :param A: wyrazy wolne dla kolejnych funkcji sklejanych
    :param B: wspolczynniki liniowe
    :param C: wspolczynniki kwadratowe
    :param D: wspolczynniki funkcji 3 rzedu
    :return: wartosci interpolowane odpowidajace x_spl
    """
    y_spl = []
    curr_p_no = 0
    curr_p = x_points[curr_p_no]
    for i in range(len(x_spl)):
        # Zmiana funkcji
        if x_spl[i] >= x_points[curr_p_no+1] and curr_p_no < len(B)-1:
            curr_p_no += 1
            curr_p = x_points[curr_p_no]

        y_spl.append(A[curr_p_no] + B[curr_p_no] * (x_spl[i]-curr_p) + C[curr_p_no] * ((x_spl[i]-curr_p)**2) + \
                     D[curr_p_no] * ((x_spl[i]-curr_p)**3))

    return y_spl

# Wczytanie danych z pliku
file = open("data.txt", 'r')
lines = file.readlines()

meas_x, meas_y = [], []
for line in lines:
    px, py = line.split()
    meas_x.append(float(px))
    meas_y.append(float(py))


# Wielomian interpolacyjny
"""
[x_0^10, x_0^9, ..., x_0^1, x_0^0               [a_10     [y_0         
.                                                 .         .   
.                                       @         .    =    .
.                                                 .         .  
x_10^10, x_10^9, ..., x_10^1, x_10^0]            a_0]      y_10]  

a_i - wspołczynniki wielomianu
"""
X = []
for i in range(len(meas_y)):
    X.append(meas_x)

X = np.array(X)
X = np.transpose(X)

for i in range(X.shape[0]):
    X[:, i] = np.power(X[:, i], X.shape[0] - i - 1)
Y = np.array(meas_y)

A = np.linalg.solve(X, Y)

# dx = meas_x[-1] - meas_x[0]
# x_plt = np.arange(start=meas_x[0] - dx*0.01, stop=meas_x[-1] + dx*0.01, step=0.05)#Pokazuje wykres nieco poza zakresem
x_pol = np.arange(start=meas_x[0], stop=meas_x[-1] + 0.05, step=0.05)
y_pol = np.array([my_polynomial(xi, A) for xi in x_pol])







# Funkcja sklejana

h = [meas_x[i + 1] - meas_x[i] for i in range(len(meas_x) - 1)]
hy = [meas_y[i + 1] - meas_y[i] for i in range(len(meas_y) - 1)]

# Wyznaczenie wspolczynnikow c_i
C_A = np.eye(11, 11)
for i in range(1, C_A.shape[0] - 1):
    C_A[i, i] = 2 * (h[i - 1] + h[i])  # Glowna przekatna
    C_A[i, i - 1] = h[i - 1]  # pod
    C_A[i, i + 1] = h[i]  # nad
finite_diffs = [hy[i] / h[i] for i in range(len(h))]

coeff = 3
C_B = [coeff * (finite_diffs[i + 1] - finite_diffs[i]) for i in range(len(finite_diffs) - 1)]
C_B.append(0.0)
C_B.insert(0, 0.0)
C_B = np.array(C_B)

C = np.linalg.solve(C_A, C_B)

# Wspolczynniki b_i
count_b = lambda f1, f0, h0, c1, c0: (f1 - f0) / h0 - h0 / 3 * (2 * c0 + c1)
B = [count_b(meas_y[i + 1], meas_y[i], h[i], C[i + 1], C[i]) for i in range(len(h))]

# Wspolczynniki d_i
count_d = lambda h0, c1, c0: (c1 - c0) / 3 / h0
D = [count_d(h[i], C[i + 1], C[i]) for i in range(len(h))]

# Wspolczynniki a_i
A_spline = meas_y

x_spl = np.arange(start=meas_x[0], stop=meas_x[-1] + 0.05, step=0.05)
y_spl = spline(x_spl, meas_x, A_spline, B, C, D)

# Rysowanie
plt.plot(meas_x, meas_y, 'o')
plt.plot(x_pol, y_pol)

plt.plot(x_spl, y_spl)

plt.legend(["Punkty", "Wielomian", "Funkcje sklejane"])
plt.show()
