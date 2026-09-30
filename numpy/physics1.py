import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

print(a + b)
print(a * b)
print(a ** b)


# Creating ARRAY
c = np.zeros(5)
print(c)
d = np.ones(5)
print(d)
e = np.arange(0, 10, 2)
print(e)
f = np.linspace(0, 1, 5)
print(f)
g = np.array([[1, 2], [3, 4]])
print(g)
h = np.eye(3)
print(h)
i = np.random.rand(3, 3)
print(i)