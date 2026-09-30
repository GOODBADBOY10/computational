import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

v0 = 20
theta = np.radians(45)
g = 10

t_land = (2 * v0 * np.sin(theta)) / g
t = np.linspace(0, t_land, 100)

x = v0 * np.cos(theta) * t
y = v0 * np.sin(theta) * t - 0.5 * g * t**2

fig, ax = plt.subplots()
ax.set_xlim(0, max(x) * 1.1)
ax.set_ylim(0, max(y) * 1.3)
ax.set_xlabel("Horizontal distance (m)")
ax.set_ylabel("Height (m)")
ax.set_title("Projectile motion (animated)")
ax.grid(True)

trail, = ax.plot([], [], 'b-', lw=1)       # the path drawn so far
ball, = ax.plot([], [], 'ro', markersize=8) # the ball itself

def update(frame):
    trail.set_data(x[:frame], y[:frame])    # draw path up to this frame
    ball.set_data([x[frame]], [y[frame]])   # move the ball to current position
    return trail, ball

ani = FuncAnimation(fig, update, frames=len(t), interval=160, blit=True)
plt.show()