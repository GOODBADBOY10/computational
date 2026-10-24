import numpy as np
import matplotlib.pyplot as plt

def simpson(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("n must be even")
    h = (b - a) / n
    x = a + h * np.arange(n + 1)
    y = f(x)
    s0 = y[0] + y[-1]        # the two ends
    s1 = y[1:-1:2].sum()     # odd points  y1, y3, ...
    s2 = y[2:-1:2].sum()     # even interior points  y2, y4, ...
    return h / 3 * (s0 + 4 * s1 + 2 * s2)

def plot_simpson(f, a, b, n, label, ax):
    """Draw the curve and the parabolas used by Simpson's rule."""
    h = (b - a) / n
    x = a + h * np.arange(n + 1)
    y = f(x)
    xx = np.linspace(a, b, 400)
    ax.plot(xx, f(xx), "b", lw=2, label=label)
    colors = ["orange", "green"]
    for k in range(0, n, 2):                    # one parabola per pair of strips
        xs, ys = x[k:k+3], y[k:k+3]
        coef = np.polyfit(xs, ys, 2)            # parabola through 3 points
        xp = np.linspace(xs[0], xs[2], 100)
        yp = np.polyval(coef, xp)
        ax.fill_between(xp, 0, yp, alpha=0.3, color=colors[(k // 2) % 2])
        ax.plot(xp, yp, "r--", lw=1.5, label="parabola" if k == 0 else None)
    ax.plot(x, y, "ro", label="points")
    ax.set_title(f"Simpson, n = {n},  I = {simpson(f, a, b, n):.6f}")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.legend()
    ax.grid(True)

# ---- Example 1: x^4 from 0 to 1, n = 2
f = lambda x: x**4
print(simpson(f, 0, 1, 2))                    # 0.208333...

# ---- Example 2: e^(-x^2) from 0 to 1, n = 10
g = lambda x: np.exp(-x**2)
print(simpson(g, 0, 1, 10))                   # 0.746825

# ---- Plots (two pictures side by side)
fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))
plot_simpson(f, 0, 1, 2,  "f(x) = x^4",      axes[0])
plot_simpson(g, 0, 1, 10, "f(x) = e^(-x^2)", axes[1])
plt.tight_layout()
plt.savefig("simpson_with_plot.png", dpi=110)
plt.show()