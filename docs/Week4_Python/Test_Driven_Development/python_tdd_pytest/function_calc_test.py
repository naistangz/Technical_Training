import unittest
from function_calc import *

from docs.Week4_Python.Test_Driven_Development.python_tdd_pytest.function_calc import Function_calc


class Calc_Test(unittest.TestCase):

    f = Function_calc()

    def test_sqrt(self):
        self.assertEqual(self.f.find_sqrt(64), 8)

    def test_find_ceil(self):
        self.assertEqual(self.f.find_ceil(90.3411), 91)


func = Function_calc
print(func.find_sqrt(16))
print(func.find_ceil(90.3411))