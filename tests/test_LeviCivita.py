import unittest
from src.utils.form_helpers import LeviCivita

class TestLeviCivita(unittest.TestCase):
    def setUp(self):
        pass

    def test_levi_civita_3d(self):
        expected_3d = {
            (0, 1, 2): 1,
            (0, 2, 1): -1,
            (1, 0, 2): -1,
            (1, 2, 0): 1,
            (2, 0, 1): 1,
            (2, 1, 0): -1
        }
        for indices, value in expected_3d.items():
            self.assertEqual(LeviCivita(3, indices), value, f"Failed for indices {indices}")

    def test_levi_civita_4d(self):
        expected_4d = {
            (0, 1, 2, 3): 1,
            (0, 1, 3, 2): -1,
            (0, 2, 1, 3): -1,
            (0, 2, 3, 1): 1,
            (0, 3, 1, 2): 1,
            (0, 3, 2, 1): -1,
            (1, 0, 2, 3): -1,
            (1, 0, 3, 2): 1,
            (1, 2, 0, 3): 1,
            (1, 2, 3, 0): -1,
            (1, 3, 0, 2): -1,
            (1, 3, 2, 0): 1,
            (2, 0, 1, 3): 1,
            (2, 0, 3, 1): -1,
            (2, 1, 0, 3): -1,
            (2, 1, 3, 0): 1,
            (2, 3, 0, 1): 1,
            (2, 3, 1, 0): -1,
            (3, 0, 1, 2): -1,
            (3, 0, 2, 1): 1,
            (3, 1, 0, 2): 1,
            (3, 1, 2, 0): -1,
            (3, 2, 0, 1): -1,
            (3, 2, 1, 0): 1
        }
        for indices, value in expected_4d.items():
            self.assertEqual(LeviCivita(4, indices), value, f"Failed for indices {indices}")


if __name__ == '__main__':
    unittest.main()