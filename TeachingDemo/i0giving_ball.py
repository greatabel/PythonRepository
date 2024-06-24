import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Heiti TC'  # 或者 'Arial Unicode MS'
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle, Rectangle

# Set up the figure, the axis, and the plot element
fig, ax = plt.subplots()

# Parameters
total_moves = 4  # Total number of moves to be made (one for each ball)
n_frames_per_move = 20  # Number of frames allocated for each move
radius = 0.2  # Radius of each ball
left_start = 4  # Starting number of balls on the left

ax.set_xlim(0, 10)
ax.set_ylim(0, 6)  # Extend y-axis to make room for text
ax.axis('off')

# Background for left and right areas
left_bg = Rectangle((0, 0), 5, 5, color='lightblue', alpha=0.5)
right_bg = Rectangle((5, 0), 5, 5, color='lightgreen', alpha=0.5)

ax.add_patch(left_bg)
ax.add_patch(right_bg)

left_balls = [Circle((1 + i, 2.5), radius, color='b') for i in range(left_start)]
right_balls = []

# Adding labels
left_label = ax.text(2.5, 5.2, '(左边)', fontsize=12)
right_label = ax.text(7.5, 5.2, '(右边)', fontsize=12)
# Assuming this is inside the same setup as before
formula_label = ax.text(5, 5.8, '左边 - 右边 =', fontsize=14, ha='center', color='red')  # Larger and red font for the label
text = ax.text(5, 5.5, '4 - 0 = 4', fontsize=14, ha='center', color='red')  # Larger and red font for the equation


def init():
    for ball in left_balls:
        ax.add_patch(ball)
    return [left_bg, right_bg, left_label, right_label, formula_label] + left_balls + [text]

def animate(i):
    move_index = i // n_frames_per_move  # Determine which ball is moving
    frame_in_move = i % n_frames_per_move  # Determine frame within the ball's move

    if move_index < total_moves:
        if frame_in_move == n_frames_per_move - 1:  # Update the formula after the ball has moved
            # Set the final position for the ball in the right area based on move_index
            new_x = 5.5 + move_index
            left_balls[move_index].center = (new_x, 2.5)
            right_balls.append(left_balls[move_index])
            # Update text after the ball has moved to the right side
            text.set_text(f'{left_start - (move_index + 1)} - {(move_index + 1)} = {left_start - 2 * (move_index + 1)}')
        elif frame_in_move < n_frames_per_move - 1:  # Move the ball to the new position gradually
            # Compute intermediate new_x during the move towards the dividing line
            new_x = 1 + move_index + (4.0 / n_frames_per_move) * frame_in_move
            left_balls[move_index].center = (new_x, 2.5)

    return [left_bg, right_bg, left_label, right_label, formula_label] + left_balls + right_balls + [text]

ani = animation.FuncAnimation(fig, animate, init_func=init,
                              frames=total_moves * n_frames_per_move, blit=False, repeat=False, interval=150)

plt.show()  # Display the animation
