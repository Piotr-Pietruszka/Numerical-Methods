""" 
Pochodna sinh x, dla x = 0.5
Obliczna zgdonie ze wzorem: 
f'(x) = (f(x+h) - f(x-h))/(2h)
"""
import numpy as np
from matplotlib import pyplot as plt
def calclulate_derivative(x0):
    size = 20

    h_den = np.arange(0, size, 1.0)
    h = 0.4*1/np.power(5, h_den)

    deriv = (np.sinh(x0+h) - np.sinh(x0-h))/(2*h)
    return deriv, h



x0 = 0.5
deriv, h = calclulate_derivative(x0)


deriv_true = np.cosh(x0)  # d/dx(sinh(x)) = cosh(x)


# Wyniki w kolumnie
error = np.absolute(deriv-deriv_true)

print(f"Wartosc prawdziwa pochodnej: {deriv_true}\n")
result = np.column_stack((h, deriv, error))
print("h, wyznaczona pochodna, wartość bezwzglęna błędu bezwzględnego")
print(result)

# Najmniejszy błąd
id_min = np.argmin(error)
print(f"h, dla ktorego błąd jest minimalny: {h[id_min]}")

# Wykres błędu od h
plt.xscale('log')
plt.yscale('log')
plt.xlabel("h - skala logarytmiczna")
plt.ylabel("error - skala logarytmiczna")

plt.scatter(h, error)
plt.show()