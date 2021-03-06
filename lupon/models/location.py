from sqlalchemy import Column, String, ForeignKey, Integer, Text, Float, JSON, Boolean, Unicode, DateTime, Table
from flask import g
from flask_login import UserMixin
from flask_sqlalchemy import Model, SQLAlchemy
from sqlalchemy.orm import relationship
from lupon import db

from .base import CustomBase
from .constants import STRING_SIZE

class Location(db.Model, CustomBase):
    '''
     Methods defined here:

    __init__(self, firstname, lastname, email, phone, locations):
        initialize class
    
    __repr__(self)
        pass

    '''
    __tablename__ = 'location'
    street = Column(String(STRING_SIZE))
    streetNumber = Column(String(STRING_SIZE))
    city = Column(String(STRING_SIZE))
    state = Column(String(STRING_SIZE))
    zip_code = Column(String(STRING_SIZE))
    #coordinates = Column(JSON)
    #customer_id = Column(Integer, ForeignKey('customer.id'))
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    contact_id = Column(Integer, ForeignKey('contact.id'), nullable=False)
    is_primary = Column(Boolean)

    def __repr__(self):
        ''' DEBUG PRINT OUTPUT'''
        # return '<Location %r>' % (self.street+" "+str(self.id))
        return '{} {}, {} {}'.format(self.street, self.streetNumber, self.city, self.zip_code) 

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'street': self.street, 
            'streetNumber': self.streetNumber,
            'city': self.city,
            'state': self.state,
            'zip_code': self.zip_code,
            'is_primary': self.is_primary,
        }