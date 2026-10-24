import numpy as np
import matplotlib.pyplot as plt

def trapezoid(f, a, b, n):
    h = (b - a) / n
    x = a + h * np.arange(n + 1)
    y = f(x)
    return h * ((y[0] + y[-1]) / 2 + y[1:-1].sum())

f = lambda x: x**2
a, b, n = 0, 1, 4

I = trapezoid(f, a, b, n)
print("Trapezoid result =", I)

# points used by the rule
h = (b - a) / n
x = a + h * np.arange(n + 1)
y = f(x)

# smooth curve for drawing
xx = np.linspace(a, b, 400)

plt.figure(figsize=(7, 4.5))
plt.plot(xx, f(xx), "b", linewidth=2, label="f(x) = x^2")

# draw each trapezoid
for i in range(n):
    plt.fill([x[i], x[i], x[i+1], x[i+1]],
             [0, y[i], y[i+1], 0],
             alpha=0.3, edgecolor="red", facecolor="orange")

plt.plot(x, y, "ro", label="points (x_i, y_i)")
plt.title(f"Trapezoidal rule, n = {n},  I = {I:.5f}")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()


# import numpy as np

# def trapezoid(f, a, b, n):
#     h = (b - a) / n
#     x = a + h * np.arange(n + 1)
#     y = f(x)
#     return h * ((y[0] + y[-1]) / 2 + y[1:-1].sum())

# f = lambda x: x**2
# I = trapezoid(f, 0, 1, 4)
# print(I)