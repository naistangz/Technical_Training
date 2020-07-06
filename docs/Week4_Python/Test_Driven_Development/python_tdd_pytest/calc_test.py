import pytest
import unittest

from calc import *

class Calc_Test(unittest.TestCase):

    simple_calc = Calc()

    def test_add(self):
        self.assertEqual(self.simple_calc.add(2, 2), 4) # Will pass if 2 + 2 is 4

    def test_subtract(self):
        self.assertEqual(self.simple_calc.subtract(3, 1), 2)

    def test_multiply(self):
        self.assertEqual(self.simple_calc.multiply(2, 2),4)

    def test_divide(self):
        self.assertEqual(self.simple_calc.divide(9,3),3)