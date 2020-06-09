#!/usr/bin/python3
"""Unittest Base class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id(self):
        b1 = Base()
        self.assertEqual((b1.id), 1)
        b2 = Base(12)
        self.assertEqual((b2.id), 12)
        b3 = Base()
        self.assertEqual((b3.id), 2)
        """b4 = Base("f"
        self.assertEqual((b4.id), "f")
        b5 = Base(-12)
        self.assertEqual((b5.id), 12)
        b6 = Base(1.5)
        self.assertEqual((b6.id), 1.5)"""
