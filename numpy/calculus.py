import numpy as np
import matplotlib.pyplot as plt

v0 = 15
a = -10
x0 = 0
t = np.linspace(0, 3, 100)  # time array from 0 to 3 seconds with 100 points
v = v0 + a * t  # velocity as a function of time. Applying the equation v = v0 + at
x = x0 + v0 * t + 0.5 * a * t**2  # position as a function of time. Applying the equation x = x0 + v0*t + 0.5*a*t^2
plt.plot(t, x)
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.title('Ball Thrown Upward')
plt.grid(True)
plt.show()

i = np.argmin(np.abs(t - 1.5))   # find the index where t is closest to 1.5
print(t[i], x[i])