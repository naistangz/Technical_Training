import unittest
from function_calc import *



class Calc_Test(unittest.TestCase):

    f = Function_calc()

    def test_sqrt(self):
        self.assertEqual(self.f.find_sqrt(64), 8)

    def test_find_ceil(self):
        self.assertEqual(self.f.find_ceil(90.3411), 91)


func = Function_calc
