from django.test import TestCase

# Create your tests here.


class PageTest(TestCase):

    def test_fail(self):
        self.assertEqual(1, 3)
