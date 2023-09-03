import numpy as np


# exception for negative bond length:
class NegativeBondLength(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


# exception for negative spring constant
class NegativeSpringConstant(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


# define the class Diatomic
class Diatomic:
    # define the constructor with four initial parameters, reduced_mass,
    # force_constant,initial_separation, initial_velocity
    def __init__(self, reduced_m, force_k, init_separation, init_velocity):
        self.reduced_mass = reduced_m
        self.force_constant = force_k
        self.init_separation = init_separation
        self.init_velocity = init_velocity

        if init_separation < 0:
            raise NegativeBondLength("Bond length cannot be negative")

        if force_k < 0:
            raise NegativeSpringConstant("Spring constant cannot be negative")

    # define the potential_energy method
    def potential_energy(self):
        return 0.5 * self.force_k * self.init_separation**2

    # define the kinetic_energy method
    def kinetic_energy(self):
        return 0.5 * self.reduced_m * self.init_velocity**2

    # define omega
    def omega(self):
        return np.sqrt(self.force_k / self.reduced_m)

    # define amplitude
    def amplitude(self):
        return np.sqrt(
            2 * (self.potential_energy() + self.kinetic_energy()) / self.force_k
        )

    # define phi
    def phi(self):
        return np.arccos(self.init_separation / self.amplitude())

    # define the analytical_position method
    def analytical_position(self, time):
        return self.amplitude() * np.cos(self.omega() * time + self.phi())

    # define the analytical_velocity method
    def analytical_velocity(self, time):
        return (
            -self.amplitude() * self.omega() * np.sin(self.omega() * time + self.phi())
        )
