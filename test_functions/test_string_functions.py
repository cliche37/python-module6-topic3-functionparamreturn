import unittest
from more_functions.string_functions import multiply_string


class StringTests(unittest.TestCase):

    def test_multiple_string(self):
        self.assertEqual("SyedSyedSyed", multiply_string("Syed", 3))
