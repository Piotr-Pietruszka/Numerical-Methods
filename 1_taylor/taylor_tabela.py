"""
 sinh x, tabela dla różnych n, gdzie n to liczba wyrazow rozwiniecia w szereg Taylora
"""
import numpy as np
import math
from matplotlib import pyplot as plt
from scipy.special import factorial

def rozw (n, x):
    counter = np.arange(0, n, 1)  # licznik
    den = np.arange(0, n, 1)  # mianownik

    counter = 2*counter + 1
    den = 2*den + 1

    counter = x**counter
    den = factorial(den)

    elements = counter/den  # elementy, rozwinięcia

    return np.sum(elements)



x = 0.5
n = 10

true_val = math.sinh(x)
print(f"true value: {true_val}")

sums = []  # rozwinięcia w szereg dla różnych n
for i in range(0, n):
    sums.append(rozw(i, x))


indexes = np.arange(0, n, 1)

error = np.full(n, true_val) - sums
relative_error = error/true_val*100

result = np.array([indexes, sums, error, relative_error])

result = np.transpose(result)

print("n, uzyskana wartosc, błąd bezwzględny, błąd względny[%]")
print(result)