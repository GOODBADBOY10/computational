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

def simpson_table(f, a, b, n, name, exact=None):
    """Print Simpson's rule step by step in a table, and return the integral."""
    if n % 2 != 0:
        raise ValueError("n must be even")
    h = (b - a) / n
    x = a + h * np.arange(n + 1)
    y = f(x)

    # weight of each point: 1 at the ends, 4 at odd j, 2 at even interior j
    w = np.ones(n + 1)
    w[1:-1:2] = 4
    w[2:-1:2] = 2

    s0 = y[0] + y[-1]
    s1 = y[1:-1:2].sum()
    s2 = y[2:-1:2].sum()
    I = h / 3 * (s0 + 4 * s1 + 2 * s2)

    line = "-" * 62
    print(f"\nSimpson's rule:  integral of {name}  from {a} to {b}")
    print(f"n = {n},  h = (b - a)/n = {h}")
    print(line)
    print(f"{'j':>3} | {'x_j':>9} | {'f(x_j)':>12} | {'weight':>6} | {'weight*f':>12}")
    print(line)
    for j in range(n + 1):
        print(f"{j:>3} | {x[j]:>9.4f} | {y[j]:>12.6f} | {int(w[j]):>6} | {w[j]*y[j]:>12.6f}")
    print(line)
    print(f"s0 (ends)           = {s0:.6f}")
    print(f"s1 (odd points)     = {s1:.6f}")
    print(f"s2 (even interior)  = {s2:.6f}")
    print(f"Sum of weight*f     = {np.sum(w*y):.6f}")
    print(f"I = (h/3)(s0 + 4 s1 + 2 s2) = ({h}/3)({s0 + 4*s1 + 2*s2:.6f})")
    print(f"I = {I:.6f}")
    if exact is not None:
        print(f"Exact value = {exact:.6f},   error = {I - exact:.2e}")
    print(line)
    return I

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

def plot_simpson_table(f, a, b, n, name, exact=None, filename=None):
    """Show Simpson's rule as a table drawn in a figure (not a graph)."""
    if n % 2 != 0:
        raise ValueError("n must be even")
    h = (b - a) / n
    x = a + h * np.arange(n + 1)
    y = f(x)

    w = np.ones(n + 1)
    w[1:-1:2] = 4
    w[2:-1:2] = 2

    s0 = y[0] + y[-1]
    s1 = y[1:-1:2].sum()
    s2 = y[2:-1:2].sum()
    I = h / 3 * (s0 + 4 * s1 + 2 * s2)

    # table contents
    col_labels = ["j", "x_j", "f(x_j)", "weight", "weight * f"]
    rows = [[j, f"{x[j]:.4f}", f"{y[j]:.6f}", int(w[j]), f"{w[j]*y[j]:.6f}"]
            for j in range(n + 1)]

    fig_h = 2.6 + 0.32 * (n + 1)
    fig, ax = plt.subplots(figsize=(8, fig_h))
    ax.axis("off")
    ax.set_title(f"Simpson's rule:  integral of {name} from {a} to {b}\n"
                 f"n = {n},  h = {h:g}", fontsize=12, fontweight="bold")

    tbl = ax.table(cellText=rows, colLabels=col_labels,
                   loc="upper center", cellLoc="center",
                   bbox=[0, 0.22, 1, 0.74])
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(10)

    # colours: header blue, weight 4 orange, weight 2 green, weight 1 grey
    shade = {4: "#ffe0b3", 2: "#cfe8cf", 1: "#e8e8e8"}
    for (r, c), cell in tbl.get_celld().items():
        if r == 0:
            cell.set_facecolor("#3b6ea5")
            cell.set_text_props(color="white", fontweight="bold")
        else:
            cell.set_facecolor(shade[int(w[r - 1])])

    summary = (f"s0 (ends) = {s0:.6f}     s1 (odd) = {s1:.6f}     s2 (even interior) = {s2:.6f}\n"
               f"I = (h/3)(s0 + 4 s1 + 2 s2) = ({h:g}/3)({s0 + 4*s1 + 2*s2:.6f}) = {I:.6f}")
    if exact is not None:
        summary += f"\nExact = {exact:.6f},   error = {I - exact:.2e}"
    fig.text(0.5, 0.02, summary, ha="center", va="bottom", fontsize=10,
             family="monospace")
    if filename:
        fig.savefig(filename, dpi=130, bbox_inches="tight")
    return fig

# ---- Example 1: x^4 from 0 to 1, n = 2   (exact = 0.2)
f = lambda x: x**4
simpson_table(f, 0, 1, 2, "x^4", exact=0.2)

# ---- Example 2: e^(-x^2) from 0 to 1, n = 10   (exact = 0.746824)
g = lambda x: np.exp(-x**2)
simpson_table(g, 0, 1, 10, "e^(-x^2)", exact=0.7468241328)

f = lambda x: x**4
g = lambda x: np.exp(-x**2)

plot_simpson_table(f, 0, 1, 2,  "x^4",      exact=0.2,          filename="table_x4.png")
plot_simpson_table(g, 0, 1, 10, "e^(-x^2)", exact=0.7468241328, filename="table_gauss.png")
plt.show()

# ---- Plots (two pictures side by side)
fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))
plot_simpson(f, 0, 1, 2,  "f(x) = x^4",      axes[0])
plot_simpson(g, 0, 1, 10, "f(x) = e^(-x^2)", axes[1])
plt.tight_layout()
plt.savefig("simpson_with_plot.png", dpi=110)
plt.show()