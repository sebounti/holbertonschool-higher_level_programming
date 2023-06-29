#!/usr/bin/python3
""" Tests module for Base Class """
import unittest
from models.base import Base


class testBaseClass(unittest.TestCase):
    """ TestBase class """

    def test_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_id2(self):
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_id3(self):
        b1 = Base(89)
        self.assertEqual(b1.id, 89)

    def test_to_json(self):
        self.assertEqual(Base.to_json_string(None), '[]')

    def test_to_json2(self):
        self.assertEqual(Base.to_json_string([]), '[]')

    def test_to_json3(self):
        list_str = Base.to_json_string([{"id": 43}])
        self.assertEqual(list_str, '[{"id": 43}]')

    def test_from_json(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json2(self):
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json3(self):
        list_str = Base.from_json_string('[{"id": 43}]')
        self.assertEqual(list_str, [{"id": 43}])

if __name__ == '__main__':
    unittest.main()
