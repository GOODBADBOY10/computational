import numpy as np
import matplotlib.pyplot as plt

v0 = 20
theta = np.radians(90)
g = 10

t_land = (2 * v0 * np.sin(theta)) / g   # general formula for landing time, same math you just did
t = np.linspace(0, t_land, 100)

x = v0 * np.cos(theta) * t
y = v0 * np.sin(theta) * t - 0.5 * g * t**2

plt.plot(x, y)
plt.xlabel("Horizontal distance (m)")
plt.ylabel("Height (m)")
plt.title("Projectile trajectory")
plt.grid(True)
plt.axis("equal")
plt.show()