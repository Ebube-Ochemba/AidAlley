#!/usr/bin/python3
"""
Initializes the models package and loads the storage engine
"""
from models.storage_factory import get_storage


storage = get_storage()
storage.reload()
