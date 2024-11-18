import unittest
import math

def get_sqrt(n):
  return math.sqrt(n)

def divide(a, b):
  return a / b

class TestUnexpected(unittest.TestCase):
  
    def test_type_error(self):
        with self.assertRaises(TypeError):
            self.assertIn('a', -1)
  