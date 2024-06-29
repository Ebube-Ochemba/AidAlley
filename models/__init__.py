#!/usr/bin/python3
"""
Factory: Chooses the storage engine based on an environment variable.
          Initializes the models package and loads the storage engine
"""
from models.engine.db_storage import DBStorage


storage = DBStorage()
storage.reload()
