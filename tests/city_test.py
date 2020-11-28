import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def setUp(self):
        self.Rome = City('Rome', 2014)
        self.Paris = City('Paris', 2014)
        self.USA = City('Washington D.C.', 2016)

    def test_can_test(self):
        self.assertEqual(True, True)

    def test_city_has_name(self):
        self.assertEqual('Rome', self.Rome.city_name)

    def test_date_of_travel(self):
        self.assertEqual(2014, self.Paris.date_of_travel)

    def test_city_not_visited(self):
        self.assertFalse(self.USA.visited) 

    def test_unsaved_city_has_None_id(self):
        self.assertIsNone(self.Paris.id)