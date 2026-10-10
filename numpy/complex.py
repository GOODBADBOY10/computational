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




# Practice Set — Complex Number Arithmetic

# Using new complex numbers this time, say $z_1 = 5 - 2i$ and $z_2 = -3 + 4i$:

# Find $z_1 + z_2$ and $z_1 - z_2$ — the basics, make sure these are automatic.
# Find $z_1 z_2$ (product) and $z_2 z_1$ — confirm they’re equal (commutative property from your notes).
# Find $z_1/z_2$ (expect a fraction, rationalize using the conjugate).
# Find $|z_1|$ and $|z_2|$ (the modulus) — this wasn’t in Question 1, but is a natural extension and appears constantly.
# Find $z_1\bar{z_2}$ and compare to $\overline{z_1}z_2$ — are they equal, or different? 
# (This tests whether you really understand conjugate rules, not just pattern-matching Question 1.)
# Find $\text{Im}(z_1^2)$ (imaginary part of a squared complex number — same idea as part (b) before, but testing Im instead of Re).
# A trickier one: if $z = x+iy$ and $z\bar{z} = 29$, 
# and you’re told $x=5$, find the two possible values of $y$. (Uses the identity $z\bar{z}=x^2+y^2$ from your notes.)
# Another common exam style: show that $(z_1+z_2)$ 
# and $\overline{z_1}+\overline{z_2}$ are related — specifically 
# verify $\overline{(z_1+z_2)} = \bar{z_1}+\bar{z_2}$ using these specific numbers 
# (this is literally Question 2 from your tutorial, 
# but doing it with actual numbers first often makes the general proof easier to understand afterward).