#!/usr/bin/python3
"""test of file model file"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid
import time


class TestBaseModel(unittest.TestCase):
    """BaseModel test"""

    def test0(self):
        """test0"""
        my_model = BaseModel()
        my_model.name = "Foued"
        my_model.my_number = 24
        mymodeldict = my_model.to_dict()
        self.assertEqual(type(mymodeldict["created_at"]), str)
        self.assertEqual(type(mymodeldict["updated_at"]), str)

    def test0_1(self):
        """type id"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        self.assertEqual(type(my_model.id), str)

    def test_1(self):
        """id checker"""
        a = BaseModel()
        a.name = "Holberton"
        a.my_number = 89
        b = BaseModel()
        b.name = "Holberton"
        b.my_number = 89
        self.assertNotEqual(a.id, b.id)

    def test_0_2(self):
        '''check update with saving'''
        fde = BaseModel()
        a = fde.updated_at
        fde.save()
        b = fde.updated_at
        self.assertNotEqual(a, b)

    def test_updatenow(self):
        '''check update with saving'''
        fde = BaseModel()
        x, y = fde.save(), datetime.utcnow()
        self.assertNotEqual(fde.updated_at, y)

    def test_1_1(self):
        """dictionnaire check"""
        d = {"__class__": "BaseModel",
             "id": uuid.uuid4(),
             "updated_at": datetime(
                 2017, 9, 28, 21, 5, 54, 119434).isoformat(),
             "created_at": datetime.now().isoformat()}
        base = BaseModel(**d)
        self.assertEqual(base.to_dict(), d)

    def test_2(self):
        """str check"""
        d = BaseModel()
        self.assertIsInstance(d.__str__(), str)

    def test_3(self):
        """str output checker"""
        tst = BaseModel()
        rslt = "[BaseModel] ({}) {}".format(tst.id, tst.__dict__)
        self.assertEqual(tst.__str__(), rslt)

    def test_4(self):
        """dict cheker"""
        d = BaseModel()
        self.assertIsInstance(d.to_dict(), dict)

    def test5(self):
        '''check instance'''
        fde = BaseModel()
        self.assertIsInstance(fde, BaseModel)

    def test6(self):
        """ to dict name """
        fde = BaseModel()
        fde.name = "Foued"
        ok = fde.to_dict()
        self.assertEqual(ok["name"], fde.name)

    def test_updatetypy(self):
        """test"""
        self.assertTrue(isinstance(BaseModel().updated_at, datetime))

    def test_save_update(self):
        """save()method."""
        a = BaseModel()
        time.sleep(0.5)
        fde = datetime.now()
        a.save()
        diff = a.updated_at - fde
        self.assertTrue(diff.total_seconds() < 0.01)


if __name__ == '__main__':
    unittest.main()
