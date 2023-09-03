# Frazis_Michael_274A_ProblemSet_1

**Custom Error: Describe the custom error that you implemented. Why did you choose this specific error,
and how is it relevant to the behavior of a diatomic molecule modeled by a harmonic oscillator?**

I chose too - to check that the force constant was always positive, as the spring must pull rather than push. 
A negative force constant would imply a net repulsive force, which is not a good
model for a chemical bond binding two atoms!

The second error was to check that the distance was not negative. In this instance
it is not physically possible, as the distance between two atoms cannot be
negative. Ofcourse, if you set an axis, the distance with respect to a particualr
frame can be negative, but we are focused on teh distance _between_ two atoms,
which must always be positive. 

**Class Limitations and Design Choices: Discuss any limitations you think exist in your Diatomic class.
Do you feel like different design choices could have been made to improve the class? If so, what are
they?**

Property Decorators:

1. Some methods defined, such as omega, amplitude, potential_energy, 
and kinetic_energy, seem more like properties of the molecule rather than 
actions it can perform. So the @property decorator might be more appropriate.

2. Some methods like amplitude are calculated each time they're called, but
force_k and reduced_m don't change. So these could be calculated once and stored.

4. Could add some checks on things like divisions to make sure they are done 
correctly.

