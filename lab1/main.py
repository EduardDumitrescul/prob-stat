import numpy as np
import matplotlib.pyplot as plt

from tema import plotPointsInsideEllipse, generatePointInsideEllipse_rectangleMethod, \
    generatePointInsideEllipse_scaleMethod


def metoda2_patrat():
    N = 1000
    plt.figure()
    plt.xlim([-1, 1])
    plt.ylim([-1, 1])
    plt.axis('equal')
    plt.title('Method 1: Random midpoint on a radius')

    n = 0
    skipped = 0
    for i in range(N):
        # theta = 2 * np.pi * np.random.rand()
        # r = np.random.rand()
        # m = np.array([r * np.cos(theta), r * np.sin(theta)])

        px = np.random.rand() * 2 - 1
        py = np.random.rand() * 2 - 1
        m = np.array([px, py])
        lm = np.sqrt(m[1] ** 2 + m[0] ** 2)

        if lm > 1:
            skipped += 1
            continue

        if lm < 1/2:
            n += 1

        a = -m[0] / m[1]
        b = m[1] - a * m[0]
        delta = 4*a**2 * b**2 - 4*(1 + a**2) * (b**2-1)
        x = np.array([(-2*a*b + np.sqrt(delta)) / (2*(a**2+1)), (-2*a*b - np.sqrt(delta)) /  (2*(a**2+1))])
        y = a*x+b

        plt.plot(x, y, 'C0', linewidth = 0.5)
        plt.plot(x, y, '.')
        plt.plot(m[0], m[1], 'C1.')

    P = n/(N - skipped)
    print('method 1: P = ', P)


def metoda3_lungimea_corzii():
    N = 100
    plt.figure()
    plt.xlim([-1, 1])
    plt.ylim([-1, 1])
    plt.axis('equal')
    plt.title('Method 3: Check chord length')

    n = 0
    skipped = 0
    for i in range(N):
        theta1 = 2 * np.pi * np.random.rand()
        theta2 = 2 * np.pi * np.random.rand()

        p1 = np.array([np.cos(theta1), np.sin(theta1)])
        p2 = np.array([np.cos(theta2), np.sin(theta2)])

        m = (p1 + p2) / 2

        chord_length = np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
        if chord_length > np.sqrt(3):
            n += 1

        a = -m[0] / m[1]
        b = m[1] - a * m[0]
        delta = 4 * a ** 2 * b ** 2 - 4 * (1 + a ** 2) * (b ** 2 - 1)
        x = np.array(
            [(-2 * a * b + np.sqrt(delta)) / (2 * (a ** 2 + 1)), (-2 * a * b - np.sqrt(delta)) / (2 * (a ** 2 + 1))])
        y = a * x + b

        plt.plot(x, y, 'C0', linewidth=0.5)
        plt.plot(x, y, '.')
        plt.plot(m[0], m[1], 'C1.')

    P = n / (N - skipped)
    print('method 1: P = ', P)


metoda3_lungimea_corzii()
plotPointsInsideEllipse(1000, 2, 3, pointGenerator=generatePointInsideEllipse_rectangleMethod)
plotPointsInsideEllipse(1000, 2, 3, pointGenerator=generatePointInsideEllipse_scaleMethod)