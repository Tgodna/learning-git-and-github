import string_utils
import unittest

class TestStringUtils(unittest.TestCase):

    def test_reverse_string(self):
        # Test reversing strings
        self.assertEqual(string_utils.reverse_string('hello'), 'olleh')
        self.assertEqual(string_utils.reverse_string('Python'), 'nohtyP')

    def test_capitalize_string(self):
        # Test capitalizing strings
        self.assertEqual(string_utils.capitalize_string('hello'), 'Hello')
        self.assertEqual(string_utils.capitalize_string('python'), 'Python')

    def test_is_capitalized(self):
        # Test checking if a string is capitalized
        self.assertTrue(string_utils.is_capitalized('Hello'))
        self.assertFalse(string_utils.is_capitalized('hello'))
        self.assertFalse(string_utils.is_capitalized('python'))
        self.assertTrue(string_utils.is_capitalized('Python'))

if __name__ == '__main__':
    unittest.main()
