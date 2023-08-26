import unittest
from src.secondary.main import secondary_main

class TestSecondary(unittest.TestCase):
    def test_secondary_main(self):
        self.assertEqual(secondary_main(), "Hello from Secondary!")
