import numpy as np
import matplotlib.pyplot as plt


def generatePointInsideEllipse_scaleMethod(r1, r2):
    radius = min(r1, r2)
    r = radius * np.sqrt(np.random.rand())
    theta = np.random.rand() * 2 * np.pi

    x = r * np.cos(theta)
    y = r * np.sin(theta)

    if radius == r1:
        y *= r2 / r1
    else:
        x *= r1 / r2

    return x, y


def generatePointInsideEllipse_rectangleMethod(r1, r2):
    while True:
        x = np.random.rand() * r1 * 2 - r1
        y = np.random.rand() * r2 * 2 - r2

        if (x ** 2) / (r1 ** 2) + (y ** 2) / (r2 ** 2) <= 1:
            return x, y

def plotPointsInsideEllipse(numberOfPoints, r1, r2, pointGenerator):
    plt.figure()
    plt.xlim([-r1, r1])
    plt.ylim([-r2, r2])
    plt.axis('equal')
    plt.title('Points Inside Ellipse')

    for i in range(numberOfPoints):
        x, y = pointGenerator(r1, r2)
        plt.plot(x, y, 'C0', linewidth=0.5)
        plt.plot(x, y, '.')


    plt.show()

