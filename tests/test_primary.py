import unittest
from src.primary.main import primary_main

class TestPrimary(unittest.TestCase):
    def test_primary_main(self):
        self.assertEqual(primary_main(), "Hello from Primary!")
