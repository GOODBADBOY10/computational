# print("Hello, physics!")
x = 10
y = 3
name = "Ademola"
ok = True
nothing = None

# print(f"{name} is {ok} but his {y} {name} is {x} and {nothing} is His")


# if x > 5:
    # print("Big")
# elif x == 5:
    # print("Equal")
# else:
    # print("Small")


# for i in range(5):
    # print(i)

# for j in range(2, 10, 2):        # start, stop and next
    # print(j)

n = 3
while n > 5:
    n -= 1

def kinetic_energy(m, v):
    return 0.5 * m * v**2
# print(kinetic_energy(2.0, 3.0))

def eat_launch(name):
    return name

# print(eat_launch("Ademola"))


nums = [1,2,3,4]
nums.append(5)
# print(nums[0], nums[-1])

point = (1.0, 2.0)
d = {
    "mass": 2.0,
    "velocity": 5.0
}
# print(d["mass"])


squares = [i**2 for i in range(10)]
evens = [i for i in range(10) if i % 2 == 0]
# print(squares)
# print(evens)

m = 10
n = 2
# print(m / n)
# print(m // n)

# ClassWork

for i in range(0, 110, 10):
    # j = 1.8 * i + 32
    j = i * 9/5 + 32
    # print(i)
    # print(j)
    print(f"The fahrenheit value of {i} is {j:.1f}F")

def gravitational_force(m1, m2, r):
    return 6.674e-11 * m1 * m2 / r**2
print(gravitational_force(5.972e24, 7.348e22, 3.844e8))

# three = [1, 3, 6, 10, 15, 21, 28, 35, 44, 54, 65, 77, 90, 104]
# for i in three:
#     print(i % 3 == 0)

triangular = [sum(range(1, n+1)) for n in range(1, 21)]  # generates the list
print(triangular)

for i in triangular:
    if i % 3 == 0:
        print(i)

planets = {
    "Mercury": 300000000,
    "Venus": 5000000000,
    "Earth": 70000.00047,
    "Mars": 8790037744,
    "Jupiter": 872944303
}
for name, mass in planets.items():
    print(name, mass)


def fibonacci(n):
    fib = [0, 1]
    for i in range(n - 2):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

print(fibonacci(10))