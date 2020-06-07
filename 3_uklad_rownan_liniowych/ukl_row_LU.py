import numpy as np
from scipy.linalg import lu

Qa = 200
Qb = 300
Qc = 150
Qd = 350

A = np.array([[-25-Qa, 25,          0,              0,       0],
              [25+Qa, -25-50-Qa-Qb, 50,             0,       0],
              [0,      50+Qa+Qb,   -50-50-25-Qa-Qb, 50,      25],
              [0,      0,           50+Qc,          -50-Qc,  0],
              [0,      0,           25+Qd,          0,       -25-Qd]])

B = -np.array([1500+Qa*2, Qb*2, 0, 0, 2500])


print("\n1) A:")
print(A)
print("\nB:")
print(B)

_, L, U = lu(A)
print("\n2) L:")
print(L)
print("\nU:")
print(U)


d_1 = np.linalg.solve(L, B)
X = np.linalg.solve(U, d_1)

print("\nX:")
print(X)

# Zmiana wektora B - nie trzeba wykonywac wszystkich obliczen od nowa
B2 = -np.array([800+Qa*2, Qb*2, 0, 0, 1200])
d_2 = np.linalg.solve(L, B2)
X2 = np.linalg.solve(U, d_2)
print("\n X (po zmianie wektora B):")
print(X2)


d1 = np.array([1, 0, 0, 0, 0])
x1 = np.linalg.solve(L, d1)
a1 = np.linalg.solve(U, x1)

d2 = np.array([0, 1, 0, 0, 0])
x2 = np.linalg.solve(L, d2)
a2 = np.linalg.solve(U, x2)

d3 = np.array([0, 0, 1, 0, 0])
x3 = np.linalg.solve(L, d3)
a3 = np.linalg.solve(U, x3)

d4 = np.array([0, 0, 0, 1, 0])
x4 = np.linalg.solve(L, d4)
a4 = np.linalg.solve(U, x4)

d5 = np.array([0, 0, 0, 0, 1])
x5 = np.linalg.solve(L, d5)
a5 = np.linalg.solve(U, x5)

A_inv = np.column_stack((a1, a2, a3, a4, a5))

print("\n4)A_inv:")
print(A_inv)
print("\nA*A_inv:")
print(np.matmul(A, A_inv))



