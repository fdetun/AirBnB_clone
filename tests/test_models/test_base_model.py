#!/usr/bin/python3
"""test of file model file"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """BaseModel test"""

    def test_1(self):
        """id"""
        a = BaseModel()
        b = BaseModel()
        self.assertNotEqual(a.id, b.id)

    def test_2(self):
        """str"""
        d = BaseModel()
        self.assertIsInstance(d.__str__(), str)

    def test_4(self):
        """dict"""
        d = BaseModel()
        self.assertIsInstance(d.to_dict(), dict)


if __name__ == '__main__':
    unittest.main()
