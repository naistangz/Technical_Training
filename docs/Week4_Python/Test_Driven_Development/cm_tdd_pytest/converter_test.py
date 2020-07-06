import pytest
import unittest

from converter import *

class Converter_Test(unittest.TestCase):

    c = Converter()

    def test_cm_to_inches(self):
        self.assertEqual(self.c.cm_to_inches(12.7),5)

    def test_inches_to_cm(self):
        self.assertEqual(self.c.inches_to_cm(10),25.4)

    def test_modulo(self):
        self.assertEqual(self.c.modulo(12, 10),2)