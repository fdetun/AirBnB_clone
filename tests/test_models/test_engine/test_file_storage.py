#!/usr/bin/python3
"""
file storage test
"""
import unittest
import time
import os
import pep8
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from datetime import datetime


class docs(unittest.TestCase):
    """Documtation Automatique test"""
    def testdocs(self):
        """docs check"""
        fde = "File Storage class"
        self.assertTrue(FileStorage.__doc__, fde)

    def testall(self):
        """ test """
        self.assertTrue(len(FileStorage.all.__doc__) > 0)

    def testnew(self):
        """ test """
        self.assertTrue(len(FileStorage.new.__doc__) > 0)

    def testreload(self):
        """ test """
        self.assertTrue(len(FileStorage.reload.__doc__) > 0)

    def testsave(self):
        """test"""
        self.assertTrue(len(FileStorage.save.__doc__) > 0)

    def test_method_docs(self):
        """docs checker"""
        fde = dir(FileStorage)
        for i in fde:
            self.assertTrue(len(i.__doc__) > 0)


class TestFileStorage(unittest.TestCase):
    """ Tests FileStorage class"""

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
        '''test of pep8'''
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

    def test_update_after(self):
        """test after update"""
        fde = FileStorage._FileStorage__objects
        file_path = FileStorage._FileStorage__file_path
        a = BaseModel()
        a.save()
        self.assertIn('BaseModel.{}'.format(a.id), fde.keys())

    def test_reload_save(self):
        """test  of JSON"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        my_model.save()
        all_objs = storage.all()
        self.assertNotEqual(my_model, all_objs)

    def test_99(self):
        """new test without args"""
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

    def test_FileStorage_path(self):
        """check the the file path"""
        self.assertTrue(isinstance(FileStorage._FileStorage__file_path, str))

    def test_10(self):
        self.assertTrue(os.access("./models/engine/file_storage.py", os.R_OK))
        self.assertTrue(os.access("./models/engine/file_storage.py", os.W_OK))
        self.assertTrue(os.access("./models/engine/file_storage.py", os.X_OK))
        self.assertTrue(os.access("./models/engine/file_storage.py", os.F_OK))

    def test11(self):
        """test"""
        os.remove("file.json")
        self.assertRaises(Exception, storage.reload())

if __name__ == '__main__':
    unittest.main()
