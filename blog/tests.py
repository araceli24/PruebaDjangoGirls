from django.test import TestCase

class SimpleTest(TestCase):

    def test_maths(self):
        self.assertEqual(1 + 2, 3)

    def test_maths_two(self):
        self.assertEqual(12, 12)