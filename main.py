import numpy as np

"""
Diatomic Model for Harmonic Motion

This module provides a class-based representation to model the behavior of a diatomic molecule based on simple harmonic motion principles. 

Classes:
    - InvalidParameterException: An exception raised for invalid parameters like negative bond length or spring constant.
    - Diatomic: Represents a diatomic molecule. It models its behavior based on the given parameters: 
      reduced mass, force constant, initial separation, and initial velocity.

The Diatomic class offers the following features:
    - Compute potential and kinetic energy of the molecule.
    - Calculate the angular frequency (omega) of oscillations.
    - Determine the amplitude of oscillations based on the molecule's energy.
    - Find the phase constant (phi) for the oscillations.
    - Predict the position and velocity of the molecule as a function of time using analytical methods.

Example Usage:
    >>> molecule = Diatomic(reduced_m=1, force_k=1, init_separation=1, init_velocity=0)
    >>> print(molecule.potential_energy)  # Get the potential energy
    >>> position_at_t = molecule.analytical_position(0.5)  # Find position at t=0.5 units

Note:
    Ensure the given parameters like initial separation and spring constant are non-negative; 
    else, an InvalidParameterException will be raised.

Dependencies:
    numpy: Used for mathematical operations such as square root, cosine, and sine functions.

"""

# exception for negative bond length:
class InvalidParameterException(Exception):
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
            raise InvalidParameterException("Bond length cannot be negative")

        if force_k < 0:
            raise InvalidParameterException("Spring constant cannot be negative")

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
