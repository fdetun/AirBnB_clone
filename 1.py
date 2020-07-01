#!/usr/bin/python3
from models import storage
import os
from models.base_model import BaseModel

fde=os.access('../README.md', os.R_OK) # Check for read access
print(fde)
