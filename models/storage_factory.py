#!/usr/bin/python3
"""
Factory Method: Chooses the storage engine based on an environment variable
"""

from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from os import getenv


def get_storage():
    storage_type = getenv("STORAGE_TYPE")
    if storage_type == 'db':
        return DBStorage()
    else:
        return FileStorage()
