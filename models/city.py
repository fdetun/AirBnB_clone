#!/usr/bin/python3
"""
State Class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    State city that inherit from BaseModel.
    """
    state_id = ""
    name = ""
