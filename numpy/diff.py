import numpy as np

def first_derivative(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

def second_derivative(f, x, h):
    return (f(x + h) - 2 * f(x) + f(x - h)) / h**2

# Example 1: f(x) = e^x at x = 0, h = 0.1
f1 = np.exp
d1 = first_derivative(f1, 0, 0.1)
d2 = second_derivative(f1, 0, 0.1)
print("Example 1: f(x) = e^x at x = 0")
print(f"  f'(0)  formula = {d1:.6f}   true = 1   error = {d1 - 1:.6f}")
print(f"  f''(0) formula = {d2:.6f}   true = 1   error = {d2 - 1:.6f}")

# Example 2: f(x) = x^3 at x = 1, h = 0.1
f2 = lambda x: x**3
d1 = first_derivative(f2, 1, 0.1)
d2 = second_derivative(f2, 1, 0.1)
print("Example 2: f(x) = x^3 at x = 1")
print(f"  f'(1)  formula = {d1:.6f}   true = 3   error = {d1 - 3:.6f}")
print(f"  f''(1) formula = {d2:.6f}   true = 6   error = {d2 - 6:.6f}")


for h in [0.1, 0.05, 0.025, 0.0125]:
    err = first_derivative(np.exp, 0, h) - 1
    print(f"h = {h:<7}  error = {err:.3e}")