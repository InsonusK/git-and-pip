import unittest
from gitandpip.functions import sum

class MyTestCase(unittest.TestCase):
    def test_call(self) :
        self.assertEqual(sum(2,3),5)