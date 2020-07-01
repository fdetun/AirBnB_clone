#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
import json
my_model = BaseModel()
my_model.name = "Holberton"
my_model.my_number = 89
my_model.save()
with open("file.json", 'r') as f:
    fde=json.load(f)
print(fde)
a = "BaseModel"+"."+my_model.id
if a in fde:
    print("foued")
print(type(fde))