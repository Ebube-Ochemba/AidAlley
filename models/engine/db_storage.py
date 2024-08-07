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

classes = {
    'Volunteer': Volunteer,
    'Event': Event,
    'EventVolunteer': EventVolunteer,
    'Notification': Notification,
    'VolunteerHours': VolunteerHours
}


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
        url = f"mysql+mysqldb://{usr}:{psswd}@{host}/{dtbs}"
        self.__engine = create_engine(url, pool_pre_ping=True)

        if getenv('AIDALLEY_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """If cls is None, queries all classes of objects.
        Return:
            Dict of queried classes, format: <class name>.<obj id> = obj.
        """
        # create new SQL query object & make object list of tables
        qry_obj = []
        if cls is None:
            for cls_name, cls in classes.items():
                qry_obj.extend(self.__session.query(cls).all())
        else:
            if isinstance(cls, str):  # Takes both str and class name
                cls = classes.get(cls)
                if not cls:
                    return {}
            qry_obj = self.__session.query(cls).all()

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

    def count(self, cls=None):
        """
        Count the number of objects in storage for a given class
        """
        if cls is None:
            total = sum(
                self.__session.query(func.count(classes[cls_name].id)).scalar()
                for cls_name in classes)
            return total
        else:
            if isinstance(cls, str):  # Takes both str and class name
                cls = classes[cls]
            return self.__session.query(func.count(cls.id)).scalar()
        
    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID,
        or None if not found
        """
        if cls is None or cls not in classes.values():
            return None
        if isinstance(cls, str):  # Takes both str and class name
            cls = classes.get(cls)
        return self.__session.query(cls).filter_by(id=id).first()
    
    def get_user_by_email(self, email):
        """Returns a user based on email"""
        return self.__session.query(Volunteer).filter_by(email=email).first()

    def get_user_by_id(self, user_id):
        """Returns a user based on id"""
        return self.__session.query(Volunteer).get(user_id)
    
    def get_event_by_id(self, event_id):
        """Returns a Event based on id"""
        return self.__session.query(Event).get(event_id)
    
    def get_user_events(self, volunteer_id):
        """Returns a list of events based on volunteer id"""
        return self.__session.query(Event).join(EventVolunteer).filter(EventVolunteer.volunteer_id == volunteer_id).all()
    
    def get_event_volunteer(self, event_id, volunteer_id):
        """Checks if a volunteer is already registered for an event"""
        return self.__session.query(EventVolunteer).filter_by(event_id=event_id, volunteer_id=volunteer_id).first()

    def get_user_notifications(self, volunteer_id):
        """Returns a list of notifications based on volunteer id"""
        return self.__session.query(Notification).filter_by(volunteer_id=volunteer_id).all()

    def get_events_created_by_user(self, user_id):
        """Returns a list of events created by a specific user"""
        return self.__session.query(Event).filter_by(creator_id=user_id).all()
    
    def get_user_hours(self, volunteer_id):
        """Returns a list of hours based on volunteer id"""
        return self.__session.query(VolunteerHours).filter_by(volunteer_id=volunteer_id).all()

    def get_volunteers_for_event(self, event_id):
        """Returns a list of volunteers registered for a specific event"""
        return self.__session.query(Volunteer).join(EventVolunteer).filter(EventVolunteer.event_id == event_id).all()
