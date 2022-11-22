import numpy as np
import matplotlib.pyplot as plt


def fact(x):
    s = 1
    for i in range(2, x + 1):
        s *= i
    return s


def func_Puasson(n):
    return n_sr ** n * e ** (-n_sr) / fact(n)


def func_Gauss(n, n_sr):
    return 1 / (2 * pi * n_sr) ** 0.5 * e ** (- (n - n_sr) ** 2 / (2 * n_sr))


def func_binom(n, N, v, size):
    return fact(N) / fact(N - n) / fact(n) * (v * v / size / size) ** n * (1 - (v * v / size / size)) ** (N - n)


e = 2.71828183
pi = 3.14159265
width = 600
height = 600
number_of_particles = 150
v = 40

n_sr = number_of_particles * v * v / width / height

print(n_sr)

oy_binom = [func_binom(i, number_of_particles, v, height) for i in range(number_of_particles // 2)]
oy_Puasson = [func_Puasson(i) for i in range(number_of_particles // 2)]
oy_Gauss = [func_Gauss(i, n_sr) for i in range(number_of_particles // 2)]

fig, ax = plt.subplots()

plt.xlabel("n")
plt.ylabel("P(n)")
ox = [i for i in range(number_of_particles // 2)]
ox_Gauss = [i for i in range(number_of_particles // 2)]

count_balls = [0.009900990099009901, 0.05480548054805481, 0.12931293129312932, 0.18351835183518353, 0.19781978197819783,
               0.1706170617061706, 0.1111111111111111, 0.0736073607360736, 0.040104010401040106, 0.021002100210021003,
               0.006000600060006, 0.0019001900190019003, 0.00030003000300030005, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
               0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
               0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
               0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

count_balls2 = [0.5246789727126806, 0.32724719101123595, 0.11215890850722311, 0.030497592295345103,
                0.005417335473515248, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

plt.plot(np.asarray(ox), np.asarray(count_balls2))
#plt.plot(np.asarray(ox), np.asarray(oy_binom))
plt.plot(np.asarray(ox), np.asarray(oy_Puasson))
#plt.plot(np.asarray(ox_Gauss), np.asarray(oy_Gauss))

ax.grid()
ax.legend(['Модельное распределение', 'Распределение Пуассона'])

plt.show()
