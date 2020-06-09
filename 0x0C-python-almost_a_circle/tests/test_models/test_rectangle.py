#!/usr/bin/python3
"""Unittest Rectangle class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id(self):
        r1 = Rectangle(10, 2)
        self.assertEqual((r1.id), 1)
        r2 = Rectangle(2, 10)
        self.assertEqual((r2.id), 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual((r3.id), 12)
        r4 = Rectangle(10, 2, 0, 0)
        self.assertEqual((r4.id), 3)

    def test_validation(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
        self.assertTrue("height must be an integer")
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.width = -10
        self.assertTrue("width must be > 0 ")
        with self.assertRaises(TypeError):
            Rectangle("10", 2)
        self.assertTrue("width must be an integer")
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.height = -10
        self.assertTrue("height must be > 0 ")
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.x = {}
        self.assertTrue("x must be an integer")
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)
        self.assertTrue("y must be >= 0")
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.y = {}
        self.assertTrue("y must be an integer")
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -1, 3)
        self.assertTrue("x must be >= 0")
