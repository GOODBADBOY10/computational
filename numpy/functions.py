import numpy as np

def kinetic_energy(m, v):
    """Kinetic energy: KE = 0.5 * m * v^2"""
    return 0.5 * m * v**2

def gravitational_force(m1, m2, r):
    """Newton's law of gravitation"""
    G = 6.674e-11
    return G * m1 * m2 / r**2

def projectile_trajectory(v0, angle_deg, g=9.81, n_points=100):
    """
    Returns t, x, y arrays for a projectile launched at speed v0 (m/s)
    and angle angle_deg (degrees), under gravity g.
    """
    theta = np.radians(angle_deg)
    t_land = (2 * v0 * np.sin(theta)) / g
    t = np.linspace(0, t_land, n_points)
    x = v0 * np.cos(theta) * t
    y = v0 * np.sin(theta) * t - 0.5 * g * t**2
    return t, x, y

def projectile_range(v0, angle_deg, g=9.81):
    """Horizontal range of a projectile."""
    theta = np.radians(angle_deg)
    return (v0**2 * np.sin(2 * theta)) / g