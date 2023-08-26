import unittest
from src.ternary.main import ternary_main

class TestTernary(unittest.TestCase):
    def test_ternary_main(self):
        self.assertEqual(ternary_main(), "Hello from Ternary!")
