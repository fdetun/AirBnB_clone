#!/usr/bin/python3
"""
file storage test
"""
import unittest
import time
import pep8
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from datetime import datetime


class TestFileStorage(unittest.TestCase):
    """ Tests FileStorage class """

    def test0(self):
        """"""
        self.assertEqual(type(storage).__name__, "FileStorage")

    def test1(self):
        """test basemodel object saving method"""
        my_model = BaseModel()
        my_model.save()
        self.assertIn("BaseModel.{}".format(
            my_model.id), storage.all().keys())

    def test_pep8(self):
        '''pep8 styling'''
        check = "Found code style errors"
        f = pep8.StyleGuide(quiet=True)
        fde = f.check_files(
            ['./models/engine/file_storage.py',
                'tests/test_models/test_engine/test_file_storage.py'])
        self.assertEqual(fde.total_errors, 0, check)

    def test_json(self):
        """test Json"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        my_model.save()
        with open("file.json", 'r') as f:
            fde = json.load(f)
        self.assertIn("BaseModel.{}".format(
            my_model.id), fde)

    def test_reload_save(self):
        """test Json"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        my_model.save()
        all_objs = storage.all()
        self.assertNotEqual(my_model, all_objs)

    def test_99(self):
        """new without args"""
        with self.assertRaises(TypeError):
            storage.new()

    def test3(self):
        """check object types"""
        a = {}
        self.assertEqual(type(FileStorage._FileStorage__objects), type(a))

    def test4(self):
        """arguments"""
        with self.assertRaises(TypeError):
            f = FileStorage(0, "sdsd", 99, 1, 8, {}, 41, 3, 1, 0, 7, [88, 1])

if __name__ == '__main__':
    unittest.main()
