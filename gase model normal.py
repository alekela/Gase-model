import pygame
from random import randint
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


class Canvas:
    def __init__(self, scene, size, v):
        self.width = size
        self.height = size
        self.region = v

    def render(self, scene, balls):
        pygame.draw.rect(scene, 'black', (0, 0, self.width, self.height), width=300)
        # pygame.draw.rect(scene, 'white', (0, 0, self.width, self.height), width=5)
        pygame.draw.rect(scene, 'yellow', ((self.width - self.region) // 2, self.height // 2 - self.region // 2,
                                        self.region, self.region), width=1)
        for ball in balls:
            pygame.draw.circle(scene, 'white', (ball.x, ball.y), 2 * ball.radius)

    def change(self, balls, count_balls, count_time, dt):
        for i in range(len(balls)):
            ball = balls[i]
            ball.move(dt)
            r = ball.radius
            if ball.x < r + 1 or ball.x > self.width - r - 1:
                ball.Vx = -ball.Vx
                ball.x = r + 1 if ball.x < self.width // 2 else self.width - r - 1
            if ball.y < r + 1 or ball.y > self.width - r - 1:
                ball.Vy = -ball.Vy
                ball.y = r + 1 if ball.y < self.width // 2 else self.width - r - 1
            for j in range(i + 1, len(balls)):
                ball2 = balls[j]
                if ball != ball2 and abs(ball.x - ball2.x) <= 2 * r + 1 and abs(ball.y - ball2.y) <= 2 * r + 1:
                    dx = (ball2.x - ball.x)
                    dy = (ball2.y - ball.y)
                    Vx = ball.Vx
                    Vy = ball.Vy
                    V2x = ball2.Vx
                    V2y = ball2.Vy
                    dy = -dy
                    Vy = - Vy
                    V2y = - V2y

                    r = (dx * dx + dy * dy) ** 0.5
                    if r == 0:
                        r = 2 * ball.radius
                    cosax = dx / r
                    sinax = (1 - cosax * cosax) ** 0.5
                    if dy < 0:
                        sinax = - sinax

                    cosay = dy / r
                    sinay = (1 - cosay * cosay) ** 0.5
                    if dx > 0:
                        sinay = -sinay

                    Vxn = Vx * cosax + Vy * sinax
                    Vyn = Vy * cosax - Vx * sinax
                    V2xn = V2x * cosax + V2y * sinax
                    V2yn = V2y * cosax - V2x * sinax

                    ball.Vx = V2xn * cosax + Vyn * sinax
                    ball.Vy = -(Vyn * cosax - V2xn * sinax)
                    ball2.Vx = Vxn * cosax + V2yn * sinax
                    ball2.Vy = -(V2yn * cosax - Vxn * sinax)
                    ball.move(5 * dt)
                    ball2.move(5 * dt)

                    """dx = (ball2.x - ball.x)
                    dy = (ball2.y - ball.y)
                    Vx = ball.Vx
                    Vy = ball.Vy
                    V2x = ball2.Vx
                    V2y = ball2.Vy
                    ball.Vx = (dx * (V2x * dx + V2y * dy) - abs(dy) * (-Vx * dy + Vy * dx)) / (
                                4 * ball.radius)
                    ball.Vy = (abs(dy) * (V2x * dx + V2y * dy) + dx * (-Vx * dy + Vy * dx)) / (
                                4 * ball.radius)
                    ball2.Vx = (dx * (Vx * dx + Vy * dy) + abs(dy) * (-V2x * dy + V2y * dx)) / (
                                4 * ball.radius)
                    ball2.Vy = (-abs(dy) * (Vx * dx + Vy * dy) + dx * (-V2x * dy + V2y * dx)) / (
                                4 * ball.radius)
                    ball.move(5 * dt)
                    ball2.move(5 * dt)"""



            if (abs(self.width // 2 - ball.x) <= self.region // 2 and abs(
                    self.height // 2 - ball.y) <= self.region // 2):
                count_balls += 1
        count_time += 1
        return count_balls, count_time


class Ball:
    def __init__(self, width, height):
        self.Vx = randint(-4000, 4000)
        self.Vy = randint(-4000, 4000)
        self.x = randint(1, width)
        self.y = randint(1, height)
        self.radius = 1

    def move(self, dt):
        self.x += self.Vx * dt
        self.y += self.Vy * dt
        #self.Vy += F / m * dt


e = 2.71828183
pi = 3.14159265
width = 600
height = 600
number_of_particles = 200
v = 40

#m = 1
#F = 0


screen = pygame.display.set_mode((width, height))
canvas = Canvas(screen, width, v)
running = True
clock = pygame.time.Clock()
balls = [Ball(width, height) for i in range(number_of_particles)]
count_balls = [0 for _ in range(number_of_particles + 1)]
all_count = 0
count = 0
count_time = 0
f = 0
fps = 100
while running:
    clock.tick(fps)
    dt = 1 / 10 / fps
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print("Экспериментальное среднее n:", all_count / count_time)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                f = 1 if f == 0 else 0
                # f = 1 ? f : 0
    if f == 1:
        count, count_time = canvas.change(balls, 0, count_time, dt)
        all_count += count
        count_balls[count] += 1
    canvas.render(screen, balls)
    pygame.display.flip()

n_sr = number_of_particles * v * v / width / height
oy_Puasson = [func_Puasson(i) for i in range(number_of_particles // 2)]

oy_Gauss = [func_Gauss(i, n_sr) for i in range(number_of_particles // 2)]
oy_binom = [func_binom(i, number_of_particles, v, height) for i in range(number_of_particles // 2)]

count_balls = [i / count_time for i in count_balls]  # нормировка до единицы

dispersion = 0
for i in range(len(count_balls)):
    dispersion += count_balls[i] * (i - n_sr) ** 2
dispersion = dispersion ** 0.5
print("Дисперсия:", dispersion)

count_balls = count_balls[:number_of_particles // 2]

fig, ax = plt.subplots()

plt.xlabel("n")
plt.ylabel("P(n)")
ox = [i for i in range(number_of_particles // 2)]
oxGauss = [i / 10 for i in range(number_of_particles // 2 * 10)]
oy_Gauss = [func_Gauss(i / 10, n_sr) for i in range(number_of_particles // 2 * 10)]

plt.plot(np.asarray(ox), np.asarray(count_balls))
plt.plot(np.asarray(ox), np.asarray(oy_binom))
print(count_balls)
#plt.plot(np.asarray(ox), np.asarray(oy_Puasson))
#plt.plot(np.asarray(oxGauss), np.asarray(oy_Gauss))
ax.grid()
ax.legend(['Модельная зависимость', 'Биномиальное распределение'])

plt.show()
