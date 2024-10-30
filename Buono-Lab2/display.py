import matplotlib.pyplot as plt
import random

def random_color():
    return (random.random(), random.random(), random.random())

def oneDimensionalGraph(subset, angularCoefficient):
    x_points = [e[0] for e in subset]
    y_points = [e[1] for e in subset]

    minx, maxx = min(x_points), max(x_points)
    xline = [minx, maxx]
    yline = [angularCoefficient*x for x in xline]

    color = random_color()
    plt.scatter(x_points, y_points, color=color, label='subset', s=50)
    plt.plot(xline, yline, color=color, label=f'One dimensional model y = {round(angularCoefficient, 3)} x')

    plt.title('Linear regression of a one dimensional model')
    plt.xlabel('X')
    plt.ylabel('Y')