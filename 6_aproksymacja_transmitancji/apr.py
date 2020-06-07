import numpy as np
import math
from scipy.optimize import fmin
from matplotlib import pyplot as plt


# Wczytanie danych z pliku
file = open("data.txt", 'r')
lines = file.readlines()

time = []
response = []

for line in lines:
    t, resp = line.split()
    time.append(t)
    response.append(resp)

time = [float(t) for t in time]
time = np.array(time)

response = [float(resp) for resp in response]
response = np.array(response)


def diff(params):
    global time, response

    k, tau_z, tau, zeta = params[0], params[1], params[2], params[3]  # Optymalizowane parametry
    s_zeta = math.sqrt(1.0-zeta**2.0)
    e_zeta = np.exp(-zeta/tau*time)

    # Odpowiedz impulsowa standardowego ukladu
    g_1 = tau_z * k * (1.0/(tau*s_zeta) * e_zeta * np.sin(s_zeta/tau*time))

    # Odpowiedz skokowa standardowego ukladu
    h_1 = k * (1.0 - 1.0/s_zeta * e_zeta * np.sin(s_zeta/tau*time + math.asin(s_zeta)))

    # Odpowiedz skokowa badanego ukladu
    h_2 = h_1 + g_1

    # Suma kwadratow roznic miedzy elemntami rzeczywistej, a estymowanej odpowiedzi
    return np.sum(np.power(response-h_2, 2))


# Minimalizacja
x0 = np.array([1.0, 1.0, 1.0, 0.1])
opt_params = fmin(diff, x0=x0)
k, tau_z, tau, zeta = opt_params[0], opt_params[1], opt_params[2], opt_params[3]
print(f"k: {k} \ntau_z: {tau_z} \ntau: {tau} \nzeta: {zeta} \n")


# Optymalna odpowiedz
s_zeta = math.sqrt(1.0-zeta**2.0)
e_zeta = np.exp(-zeta/tau*time)
g_1_opt = tau_z * k * (1.0/(tau*s_zeta) * e_zeta * np.sin(s_zeta/tau*time))
h_1_opt = k * (1.0 - 1.0/s_zeta * e_zeta * np.sin(s_zeta/tau*time + math.asin(s_zeta)))
h_2_opt = h_1_opt + g_1_opt


plt.plot(time, response)
plt.plot(time, h_2_opt)
plt.legend(["Pomiary", "Aproksymacja"])
plt.show()
