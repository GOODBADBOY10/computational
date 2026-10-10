import numpy as np

z1 = 4 + 3j
z2 = 2 - 5j

# (a) z1 * z2
print("z1 * z2 = ", z1 * z2)

# (b) Re(z1^3) and (Re z1)^3
z1_cubed = z1 ** 3
print("z1^3 = ", z1_cubed)
print("Re(z1^3) = ", z1_cubed.real)
print("(Re z1)^3 = ", (z1.real) ** 3)

# (c) (z1 - z2) / (z1 + z2)
print("(z1-z2)/(z1+z2) =", (z1 - z2) / (z1 + z2))

# (d) z1 * conjugate(z1), and conjugate(z1) * z2
print("z1 * conj(z1) = ", z1 * np.conj(z1))
print("conj(z1) * z2 = ", np.conj(z1) * z2)


# (e) conj(z1)/conj(z2), and conjugate of (z1/z2)
print("conj(z1)/conj(z2) =", np.conj(z1) / np.conj(z2))
print("conj(z1/z2) =", np.conj(z1 / z2))