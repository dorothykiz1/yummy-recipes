from myapp.models.dashboard import Dashboard
import unittest

class TestDashBoard(unittest.TestCase):
    def setUp(self):
        self.dashboard = Dashboard()


    def test_signup_is_successful(self):
        self.assertEqual(len(self.dashboard.registry), 0)
        self.assertTrue(self.dashboard.signup("testing tester", "tester@gmail.com", "testersPassword"))
        self.assertEqual(len(self.dashboard.registry), 1)
        self.assertIsNotNone(self.dashboard.registry["tester@gmail.com"])
