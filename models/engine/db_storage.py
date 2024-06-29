#!/usr/bin/python3
"""
Contains the DBStorage class for the AidAlley project
"""

from models.base_model import Base
from models.event import Event
from models.event_volunteer import EventVolunteer
from models.notification import Notification
from models.volunteer import Volunteer
from models.volunteer_hours import VolunteerHours
from os import getenv
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker, scoped_session

classes = [Volunteer, Event, EventVolunteer, Notification, VolunteerHours]


class DBStorage:
    """This class manages storage of AidAlley models in a database"""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage"""
        usr = getenv("AIDALLEY_MYSQL_USER")
        psswd = getenv("AIDALLEY_MYSQL_PWD")
        host = getenv("AIDALLEY_MYSQL_HOST")
        dtbs = getenv("AIDALLEY_MYSQL_DB")
        url = "mysql+mysqldb://{}:{}@{}/{}".format(usr, psswd, host, dtbs)
        self.__engine = create_engine(url, pool_pre_ping=True)

        if getenv('AIDALLEY_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """If cls is None, queries all classes of objects.
        Return:
            Dict of queried classes, format: <class name>.<obj id> = obj.
        """
        if not cls:  # create new SQL query object & make object list of tables
            qry_obj = []
            qry_obj.extend(self.__session.query(Event))
            qry_obj.extend(self.__session.query(EventVolunteer))
            qry_obj.extend(self.__session.query(Notification))
            qry_obj.extend(self.__session.query(Volunteer))
            qry_obj.extend(self.__session.query(VolunteerHours))
        else:
            qry_obj = self.__session.query(cls)

        result = {'{}.{}'.format(type(obj).__name__, obj.id):
                  obj for obj in qry_obj}
        return result

    def new(self, obj):
        """Adds an object to the current db session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes 'obj' from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Call remove() method on self.__session"""
        self.__session.remove()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID,
        or None if not found
        """
        if cls not in classes:
            return None

        return self.__session.query(cls).filter_by(id=id).first()
    
    def count(self, cls=None):
        """
        Count the number of objects in storage for a given class
        """
        if cls is None:
            return sum(self.count(cls) for cls in classes)
        else:
            return self.__session.query(func.count(cls.id)).scalar()
