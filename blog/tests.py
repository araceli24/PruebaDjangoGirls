from django.test import TestCase

class SimpleTest(TestCase):

    def test_maths(self):
        self.assertEqual(1 + 2, 3)

    def test_upper(self):
        self.assertEqual('ara'.upper(), 'ARA')

    