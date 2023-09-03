import unittest
from main import Diatomic


class TestDiatomic(unittest.TestCase):
    def setUp(self):
        self.diatomic = Diatomic(
            1, 1, 1, 1
        )  # example values, chose to make calculations easier

    def test_initializaition(self):
        self.assertEqual(self.diatomic.reduced_mass, 1)
        self.assertEqual(self.diatomic.force_constant, 1)
        self.assertEqual(self.diatomic.initial_separation, 1)
        self.assertEqual(self.diatomic.initial_velocity, 1)

    def test_potential_energy(self):
        self.assertEqual(self.diatomic.potential_energy(), 0.5)

    def test_kinetic_energy(self):
        self.assertEqual(self.diatomic.kinetic_energy(), 0.5)

    def test_analytical_position(self):
        self.assertAlmostEqual(self.diatomic.analytical_position(1), 1.0806046117362795)

    def test_analytical_velocity(self):
        self.assertAlmostEqual(
            self.diatomic.analytical_velocity(1), -1.3817732906760363
        )

    if __name__ == "__main__":
        unittest.main()
