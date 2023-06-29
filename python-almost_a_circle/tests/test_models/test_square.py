#!/usr/bin/python3
""" Square class tests module """

from models.square import Square
import unittest
import os


class testSquareClass(unittest.TestCase):
    """ Test Square class """

    def set_up(self):
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_square_0(self):
        s1 = Square(1)
        self.assertEqual(s1.size, 1)
        s1 = Square(1, 2)
        self.assertEqual(s1.x, 2)
        s1 = Square(1, 2, 3)
        self.assertEqual(s1.y, 3)
        s1 = Square(1, 2, 3, 4)
        self.assertEqual(s1.id, 4)

    def test_square_1(self):
        s1 = Square(1, 0, 0, 43)
        self.assertEqual(s1.__str__(), '[Square] (43) 0/0 - 1')

        dic = {"id": 43, "size": 1, "x": 0, "y": 0}
        self.assertEqual(s1.to_dictionary(), dic)

    def test_square_update(self):
        s1 = Square(1)
        s1.update(89, 1, 2, 3)
        self.assertEqual(s1.id, 89)

    def test_square_create(self):
        dic = {'id': 89, 'size': 1, 'x': 2, 'y': 3}
        s1 = Square.create(**dic)
        self.assertEqual(s1.id, 89)

    def test_square_save_0(self):
        Square.save_to_file(None)
        with open("Square.json") as f:
            self.assertEqual(f.read(), '[]')

    def test_square_save_1(self):
        Square.save_to_file([])
        with open("Square.json") as f:
            self.assertEqual(f.read(), '[]')

    def test_square_save_2(self):
        Square.save_to_file([Square(1, 0, 0, 43)])
        expected = '[{"id": 43, "size": 1, "x": 0, "y": 0}]'
        with open("Square.json") as f:
         #   self.assertEqual(f.read(), expected)

    def test_squate_load_0(self):
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        s1 = Square.load_from_file()
        self.assertEqual(s1, [])

    def test_square_load_1(self):
        Square.save_to_file([Square(1, 0, 0, 43)])
        s1 = Square.load_from_file()
        self.assertEqual(s1[0].id, 43)

    def test_square_errors(self):
        self.assertRaises(TypeError, Square, "1")
        self.assertRaises(TypeError, Square, 1, "1")
        self.assertRaises(TypeError, Square, 1, 1, "1")
        self.assertRaises(ValueError, Square, -1)
        self.assertRaises(ValueError, Square, 1, -1)
        self.assertRaises(ValueError, Square, 1, 1, -43)
        self.assertRaises(ValueError, Square, 0)
