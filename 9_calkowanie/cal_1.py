# Skrypt oblicza całkę z wielomianu (wzór w pol_arr), pomiędzy punktami x1 i x2
# metodą: Romberga i przy użyciu trzypunktowej kwadratury Gaussa
# Dla porównania całka jest również liczona analitycznie

import numpy as np
from math import sqrt


# Funkcja do scalkowania
pol_integrand = lambda x: 0.062561*(x**4) - 0.7825*(x**3) + 0.1322*(x**2) - 4.61*x + 1.27
pol_arr = lambda x: 0.062561*np.power(x, 4) - 0.7825*np.power(x, 3) + 0.1322*np.power(x, 2) - 4.61*x + 1.27


def trapez_integ(x1, x2, h):
    """
    Liczenie calki z wielomianu pol_arr metoda trapezow
    :param x1: punkt startowy
    :param x2: punkt koncowy
    :param h: krok calkowania
    :return: wynik calki
    """
    x = np.arange(x1, x2, h)
    y = pol_arr(x)

    results = h * (y[:-1] + y[1:]) / 2.0
    result = np.sum(results)
    return result


if __name__ == "__main__":

    x1 = -4
    x2 = 13

    # Rozwiazanie analityczne
    # --------------------------------------------------
    a = [0.062561/5, -0.7825/4, 0.1322/3, -4.61/2, 1.27]
    integral_analytical_func = lambda x: a[0]*(x**5) + a[1]*(x**4) + a[2]*(x**3) + a[3]*(x**2) + a[4]*x

    int_analytical = integral_analytical_func(x2) - integral_analytical_func(x1)
    # print(f"Wynik calkowania analitycznego: {int_analytical}")
    print(f"Wielomian wynikowy: {a[0]}*(x**5) + {a[1]}*(x**4) + {a[2]}*(x**3) + {a[3]}*(x**2) + {a[4]}*x\n\n")
    # --------------------------------------------------

    # metoda Romberga
    # --------------------------------------------------
    integrals_Romb = [[]]  # Przechowywane wyniki calek

    # Pierwsza wartosc calki
    h = 1
    new_integral = trapez_integ(x1, x2, h)
    integrals_Romb[0].append(new_integral)

    err_threshold = 0.002  # Dopuszczalny blad wzgledny - kryterium stopu
    err = 100
    while err > err_threshold:
        integrals_Romb.append([])  # Calki o wiekszym rzedzie bledu
        h = h*0.5

        new_integral = trapez_integ(x1, x2, h)  # Policzenie calki metoda trapezow, z coraz mnijeszym przedzialem

        # Dolaczenie do calek o bledzie rzedu h**2
        integrals_Romb[0].append(new_integral)

        # Liczenie calek o bledach wyzszych rzedow
        for i in range(len(integrals_Romb)-1):
            a = (4.0**(i+1)*integrals_Romb[i][-1] - integrals_Romb[i][-2]) / (4.0**(i+1)-1)
            integrals_Romb[i+1].append(a)

            if i == len(integrals_Romb)-2:
                # Szacowanie aktualnego bledu
                err = abs((integrals_Romb[i+1][0] - integrals_Romb[i][1]) / integrals_Romb[i+1][0])


    result_Romberg = integrals_Romb[-1][0]
    # --------------------------------------------------

    # trzypunktowa kwadratura Gaussa
    # --------------------------------------------------
    # punkty do szacowania i wspolczynniki wartosci funkcji w tych punktach
    x_G0, x_G1, x_G2 = -sqrt(3.0 / 5.0), 0.0, sqrt(3.0 / 5.0)
    c0, c1, c2 = 5.0 / 9.0, 8.0 / 9.0, 5.0 / 9.0

    # podstawienie - w celu zamiany przedzialu calkowania na [-1, 1]
    d_substitution = (x2-x1)/2
    variable_substitution = lambda x: ((x2+x1) + (x2-x1)*x)/2

    x_G0, x_G1, x_G2 = variable_substitution(x_G0), variable_substitution(x_G1), variable_substitution(x_G2)

    # Wynik calki
    result_Gauss = c0*pol_integrand(x_G0)*d_substitution + c1*pol_integrand(x_G1)*d_substitution + c2*pol_integrand(x_G2)*d_substitution

    # --------------------------------------------------

    # Wyniki
    results_all = integrals_Romb[:]
    results_all.insert(0, "Metoda Romberga (kolejne rzedy to bledy o rzedach kolejno h**2, h**4, ...). Ostatni rzead zawiera wynik ostateczny: ")

    results_all.insert(0, int_analytical)
    results_all.insert(0, "Wynik calkowania analitycznego: ")

    results_all.append("Wynik calkowania za pomoca trzypunktowej kwadratury Gaussa: ")
    results_all.append(result_Gauss)
    for i in results_all:
        print(i)



