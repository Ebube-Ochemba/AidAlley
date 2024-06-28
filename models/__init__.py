#!/usr/bin/python3
"""
Factory: Chooses the storage engine based on an environment variable.
          Initializes the models package and loads the storage engine
"""
from os import getenv


storage_type = getenv("AIDALLEY_STORAGE_TYPE")

if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
