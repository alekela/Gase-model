from tkinter import *
from math import *
from random import *

okno = Tk()
okno.geometry('600x600')
holst = Canvas(okno, width=600, height=600, bg='white')
holst.pack()
a = 10
A = 300
r = 1
balls = []
X = []
Y = []
Vx = []
Vy = []
counter = 0
scounter = 0
numcounter = 0
for i in range(r, 2 * A - r, 20 * r):
    for j in range(r, 2 * A - r, 20 * r):
        Y.append(j)
        X.append(i)
        Vx.append(randint(-1000, 1000))
        Vy.append(randint(-1000, 1000))
        balls.append(holst.create_oval(i - r, j - r, i + r, j + r))
dt = 0.01
num = len(X)
for _ in range(1000):
    counter = 0
    for i in range(num):
        dx = Vx[i] * dt
        dy = Vy[i] * dt
        X[i] += dx
        Y[i] += dy
        if (X[i] > 2 * A) or (X[i] < 0):
            Vx[i] *= (-1)
        if (Y[i] > 2 * A) or (Y[i] < 0):
            Vy[i] *= (-1)
        holst.coords(balls[i], X[i] - r, Y[i] - r, X[i] + r, Y[i] + r)
        holst.update()
        if (abs(X[i] - A) < a / 2 and abs(Y[i] - A) < a / 2):
            counter += 1
    scounter += counter
    numcounter += 1
print(scounter / 1000)
