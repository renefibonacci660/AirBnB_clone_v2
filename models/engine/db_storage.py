#!/usr/bin/python3
"""This is the file storage class for AirBnB"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
"""
class DBStorage:
    '''

    '''

    __engine = None
    __session = None

    
    def __init__(self):
    '''

    '''
        user = os.getenv("HBNB_MYSQL_USER")
        passwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")

        connection = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
        self.__engine = create_engine(connection.format(user, passwd, host, db),
                                      pool_pre_ping=True)

        ''' Deleting everything we just connected to in self.__engine'''
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''
        '''
        all_classes = ['User', 'State', 'City', 'Amenity', 'Place', 'Review']
        obj_dict, obj_list = {}, []
        if cls is None:
            for each_class in all_classes:
                for obj in self.__session.query(eval(each_class)):
                    obj_list.append(obj)
        else:
            for obj in self.__session.query(eval(cls)):
                obj_list.append(obj)
        for obj in obj_list:
            obj_dict[type(obj).__name__ + "." + str(obj.id)] = obj
        return obj_dict

    def new(self, obj):
        """Add an object to the database session"""
        if obj:
            self.__session.add(obj)
  
