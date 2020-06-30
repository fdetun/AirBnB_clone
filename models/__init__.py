#!/usr/bin/python3
"""
"""
from .engine import file_storage
# from .base_model import BaseModel
"""
create the variable storage, an instance of FileStorage
"""
storage = file_storage.FileStorage()
"""
call reload() method on this variable
"""
storage.reload()
