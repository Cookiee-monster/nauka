from kat_miedzy_wskazówkami import input_data, kat_godziny, kat_minuty

import unittest

class KatTest(unittest.TestCase):
    def test_kat_godziny_12(self):
        self.assertEqual(kat_godziny(12), 360)

    def test_kat_godziny_15_15(self):
        self.assertEqual(kat_godziny(15,15), 97.5)

    def test_kat_godziny_26_00(self):
        kat_godziny(26)
        self.assertRaises(ValueError)

    def test_kat_godziny_12_30(self):
        self.assertEqual(kat_godziny(12, 30), 165)

if __name__ == "__main__":
    unittest.main()