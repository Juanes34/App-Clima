from django.test import TestCase
import unittest
from views import get_location
# Create your tests here.

class testeo_get_locations(unittest.TestCase):
    def prueba1(self):
        testcase = "Bogotá"
        expected = ("Bogota","Bogotá")
        self.assertEqual(get_location(testcase),expected)

unittest.main(argv=['first-argv-ignored'],exit=False)