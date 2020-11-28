import unittest
from models.country import Country

class TestCountry(unittest.TestCase):
    def setUp(self):
        self.Italy= Country('Italy')
        self.France = Country('France')
        self.USA = Country('USA')

    def test_can_test(self):
        self.assertEqual(True, True)

    def test_country_has_name(self):
        self.assertEqual('Italy', self.Italy.name)

    def test_unsaved_country_has_None_id(self):
        self.assertIsNone(self.USA.id)
    