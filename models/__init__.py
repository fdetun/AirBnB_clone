#!/usr/bin/python3
"""
importing file_storage.
"""
from models.engine import file_storage

storage = file_storage.FileStorage()

storage.reload()
