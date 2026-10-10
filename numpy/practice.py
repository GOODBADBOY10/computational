import numpy as np

def average_speed(distance, time):
    return distance / time

trips = [(100, 2), (250, 5), (60, 1.5)]   # (distance in km, time in hours)
for trip in trips:
    print(average_speed(trip))


angles = np.linspace(0, 360, 100)
theta = np.radians(angles)
sine_of_each = np.sin(theta)
print(sine_of_each)
print(sine_of_each > 0.5)