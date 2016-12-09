import matplotlib.pyplot as plt


def draw_graph(x, y):
    plt.plot(x, y, marker='o')
    plt.xlabel('Distance in meters')
    plt.ylabel('G force in newtons')
    plt.title(
        'G force and distance'
        )
    plt.show()


def generate_F_r():
    # Generate values for r
    r = range(100, 1001, 50)
    # Empty list to store the calculated values of F
    F = []
    # Constant, G
    G = 6.674*(10**-11)
    # Two masses
    m1 = 0.5
    m2 = 1.5
    for dist in r:
        force = G*(m1*m2)/(dist**2)
        F.append(force)
    draw_graph(r, F)

if __name__ == '__main__':
    generate_F_r()
