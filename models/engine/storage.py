#!/usr/bin/python3
"""This is a boilerplate class for storage engines"""

from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def save(self, obj):
        pass

    @abstractmethod
    def delete(self, obj):
        pass

    @abstractmethod
    def get(self, cls, id):
        pass

    @abstractmethod
    def all(self, cls):
        pass

    @abstractmethod
    def reload(self):
        pass
