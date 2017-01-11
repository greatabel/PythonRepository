import matplotlib.pyplot as plt
import math

g = 9.8

def frange(start, final, increment):
    numbers = []
    while start < final:
        numbers.append(start)
        start = start + increment
    return numbers

def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('Projectile motion at different initial velocities(速度) and angles(角度)')
    plt.show()

def draw_trajectory(u, theta, t_flight):
    x = []
    y = []
    intervals = frange(0, t_flight, 0.001)
    for t in intervals:
        x.append(u*math.cos(theta)*t)
        y.append(u*math.sin(theta)*t - 0.5*g*t*t)

    draw_graph(x, y)

if __name__ == "__main__":
    draw_trajectory(10, 0.1, 5)