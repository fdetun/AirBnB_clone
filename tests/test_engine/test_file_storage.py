#!/usr/bin/python3
"""
file storage test 
"""

import unittest
import time
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime

class TestFileStorage(unittest.TestCase):
    """ Tests FileStorage class """

    def test0(self):
        """files exist"""
        self.assertFalse(os.path.exists("file.json"))

    def test1(self):
        pass

    def test2(self):
        """"""
        self.assertEqual(type(storage).__name__, "FileStorage")

    def test3(self):
        """check object types"""
        a = {}
        self.assertEqual(type(FileStorage._FileStorage__objects), type(a))

    def test4(self):
        """arguments"""
        with self.assertRaises(TypeError):
            f = FileStorage(0,"sdsd",99,1,1,1,1,1,1,1,1,[88, 1])

if __name__ == '__main__':
    unittest.main()
