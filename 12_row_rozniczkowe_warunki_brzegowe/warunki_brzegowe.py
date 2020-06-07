"""
Rownanie rozniczkowe (opisujace rozklad temperatury w stanie ustalonym):
d2T(x,y)/dx2 + d2T(x,y)/dy2 + h'(Ta - T(x,y)) = 0
Ta - temeperatura otoczenia
h' - stala
dane warunki brzegowe Dirichleta



Przyblizenia:
d2T(x,y)/dx2 = (T(x-dx,y) - 2T(x,y) + T(x+dx,y))/(dx^2)
d2T(x,y)/dy2 = (T(x,y-dy) - 2T(x,y) + T(x,y+dy))/(dy^2)

Wykorzystujac przyblizenia (i fakt, że dy=dx)
-(4/dx^2 + h')*T(x,y) + 1/dx^2 * (T(x-dx,y) + T(x+dx,y) + T(x,y-dy) + T(x,y+dy)) = -h' * Ta
"""
import numpy as np
import matplotlib.pyplot as plt

side_size = 9
total_size = side_size*side_size

h_p = 0.05
T_a = 100  # Temperatura otoczenia
dx = 2.0  # Krok przestrzenny

# Wektor b, otoczenie
b = -h_p*T_a*np.ones((81, 1))

# Macierz A
A = -((4.0/(dx*dx) + h_p)*np.eye(total_size))

coef = 1/(dx*dx)

# Uwzglednienie wezlow sasiednich: w macierzy A oraz jako warunki brzegowe dla skrajnych wartosci
for i in range(0, A.shape[0]):
    # Pierwszy rzad
    if i >= side_size:
        A[i][i - side_size] = coef  # T(x,y-dy)
    else:
        b[i] -= coef*(400 - (i+1)*10)  # warunki brzegowe dla piewrszego rzedu

    # Ostatni rzad
    if i < A.shape[0]-side_size:
        A[i][i + side_size] = coef  # T(x,y+dy)
    else:
        b[i] -= coef*(300 - (i%side_size+1)*10)  # warunki brzegowe dla ostatniego rzedu

    # Pierwsza kolumna
    if i % side_size != 0:
        A[i][i-1] = coef  # T(x-dx,y)
    else:
        b[i] -= coef*(400 - int(i/side_size+1)*10)  # warunki brzegowe dla pierwzej kolumny

    # Ostatnia kolumna
    if i % side_size != side_size-1:
        A[i][i+1] = coef  # T(x+dx,y)
    else:
        b[i] -= coef*(300 - int(i/side_size+1)*10)  # warunki brzegowe dla ostatniej kolumny

x = np.linalg.solve(A, b)





x = np.reshape(x, (side_size, side_size))
plt.imshow(x, cmap='hot')
plt.xlabel("X/2")
plt.ylabel("Y/2")

plt.colorbar()

plt.show()



