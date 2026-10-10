import numpy as np

def to_polar(z, label):
    r = abs(z)
    theta = np.angle(z)
    print(f"{label}: z = {z}")
    print(f"   r (modulus) = {r}")
    print(f"   theta (radians) = {theta}")
    print(f"   theta (degrees) = {np.degrees(theta)}")
    print()

# (i) 1 + i
z_i = 1 + 1j
to_polar(z_i, "(i) 1+i")

# (ii) (1-i)/(1+i)
z_ii = (1 - 1j) / (1 + 1j)
to_polar(z_ii, "(ii) (1-i)/(1+i)")

# (iii) ((6+8i)/(4-3i))^2
z_iii = ((6 + 8j) / (4 - 3j)) ** 2
to_polar(z_iii, "(iii) ((6+8i)/(4-3i))^2")

# (iv) (2+i)/(5-3i)
z_iv = (2 + 1j) / (5 - 3j)
to_polar(z_iv, "(iv) (2+i)/(5-3i)")

# (v) (7-5i)/(4i)
z_v = (7 - 5j) / (4j)
to_polar(z_v, "(v) (7-5i)/(4i)")