import matplotlib.pyplot as plt
import math


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
    # plt.show()


if __name__ == "__main__":
    # draw_graph(10, 10)