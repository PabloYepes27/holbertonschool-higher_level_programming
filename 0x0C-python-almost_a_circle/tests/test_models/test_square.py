#!/usr/bin/python3
"""Unittest Square class"""
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id(self):
        r1 = Square(10)
        self.assertEqual((r1.id), 1)
        r2 = Square(2, 10)
        self.assertEqual((r2.id), 2)
        r3 = Square(2, 0, 0, 12)
        self.assertEqual((r3.id), 12)
