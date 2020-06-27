from pylab import *
from cmath import *

m, n = 4, 3

A = zeros((m, n), dtype=complex)
Q, R = zeros((m, n), dtype=complex), zeros((n, n), dtype=complex)

for i in range(0, m):
    for j in range(0, n):
        r = randint(-10, 10)  # int(input("Enter the value of real A["+str(i)+"]["+str(j)+"]"))
        c = randint(-10, 10)  # int(input("Enter the value of complex A["+str(i)+"]["+str(j)+"]"))
        A[i][j] = complex(r, c)

print("A = ")
print(A)

for i in range(0, n):
    u = A[:, i]
    for j in range(0, i):
        u = u - dot(u, conj(Q[:, j])) * Q[:, j]
    Q[:, i] = u / sqrt(dot(u, conj(u)))

print("Q = ")
print(Q.round(decimals=3))

R = dot(Q.transpose(), conj(A))

print("R = ")
print(R.round(decimals=3))

print("QR = ")
print(dot(Q, conj(R)).round(decimals=3))

print(qr(A))
