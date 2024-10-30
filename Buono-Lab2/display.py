import matplotlib.pyplot as plt
import random

def random_color():
    return (random.random(), random.random(), random.random())

def oneDimensionalGraph(subset, angularCoefficient, offset):
    colour = random_color()

    x_points = [e[0] for e in subset]
    y_points = [e[1] for e in subset]
    plt.scatter(x_points, y_points, color=colour, label='subset', s=50)

    minx, maxx = min(x_points), max(x_points)
    xline = [minx, maxx]
    if angularCoefficient == None: plt.axvline(x=x_points[0], color=colour, linestyle='-', label=f'One dimensional model x = {x_points[0]}')
    else: 
        yline = [angularCoefficient*x + offset for x in xline]
        plt.plot(xline, yline, color=colour, label=f'One dimensional model y = {round(angularCoefficient, 3)} x')

    plt.title('Linear regression of a one dimensional model')
    plt.xlabel('X')
    plt.ylabel('Y')