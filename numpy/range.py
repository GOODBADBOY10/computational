import numpy as np
import matplotlib.pyplot as plt
from functions import projectile_trajectory, projectile_range

t, x, y = projectile_trajectory(v0=20, angle_deg=45)

plt.plot(x, y)
plt.xlabel("Horizontal distance (m)")
plt.ylabel("Height (m)")
plt.title("Projectile trajectory")
plt.grid(True)
plt.axis("equal")
plt.show()

print("Range:", projectile_range(v0=20, angle_deg=45))