import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

A = 5
omega = 2

t = np.linspace(0, 10, 500)
x = A * np.cos(omega * t)

wall_x = -8   # fixed point the spring is anchored to

fig, ax = plt.subplots()
ax.set_xlim(wall_x - 1, A * 1.3)
ax.set_ylim(-2, 2)
ax.set_xlabel("Position (m)")
ax.set_yticks([])
ax.set_title("Mass on a spring (SHM)")
ax.axvline(0, color='gray', linestyle='--', linewidth=1)
ax.axvline(wall_x, color='black', linewidth=4)   # draws the wall

mass, = ax.plot([], [], 'ro', markersize=20)
spring, = ax.plot([], [], 'b-', linewidth=1.5)

def make_spring(x_start, x_end, n_coils=12, amplitude=0.4):
    """Generate zigzag points between the wall and the mass."""
    xs = np.linspace(x_start, x_end, n_coils * 2)
    ys = amplitude * np.tile([1, -1], n_coils)   # alternate up/down
    ys[0] = 0     # start flat at the wall
    ys[-1] = 0    # end flat at the mass
    return xs, ys

def update(frame):
    mass.set_data([x[frame]], [0])
    xs, ys = make_spring(wall_x, x[frame])
    spring.set_data(xs, ys)
    return mass, spring

ani = FuncAnimation(fig, update, frames=len(t), interval=20, blit=False)
plt.show()


# import numpy as np
# import matplotlib.pyplot as plt

# A = 5           # amplitude, m
# omega = 2       # angular frequency, rad/s

# t = np.linspace(0, 10, 500)   # 10 seconds, plenty of oscillations

# x = A * np.cos(omega * t)
# v = -A * omega * np.sin(omega * t)
# a = -A * omega**2 * np.cos(omega * t)

# plt.plot(t, x, label="position x(t)")
# plt.plot(t, v, label="velocity v(t)")
# plt.xlabel("Time (s)")
# plt.ylabel("Value")
# plt.title("Simple Harmonic Motion")
# plt.legend()
# plt.grid(True)
# plt.show()