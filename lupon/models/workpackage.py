from sqlalchemy import Column, String, ForeignKey, Integer, Text, Float, JSON, Boolean, Unicode, DateTime, Table, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from lupon import db
from flask import jsonify

from .base import CustomBase
from .constants import STRING_SIZE


association_table = Table('association', db.Model.metadata,
    Column('workpackage_id', Integer, ForeignKey('workpackage.id'), primary_key=True),
    Column('task_id', Integer, ForeignKey('task.id'), primary_key=True)
)

''' association_table = Table('workpackage_task', Base.metadata,
    Column('workpackage_id', Integer, ForeignKey('workpackage.id')),
    Column('task_id', Integer, ForeignKey('task.id')) ) '''



class Workpackage(db.Model, CustomBase):
    
    __tablename__ = 'workpackage'
    name = Column(String(STRING_SIZE))
    description = Column(Text)
    due_date = Column(DateTime())
    start_date = Column(DateTime())
    status = Column(String(STRING_SIZE))
    is_active = Column(Boolean)
    discount = Column(Float)
    priority = Column(String(STRING_SIZE))
    # comment = Column(Text)
    location_id = Column(Integer, ForeignKey('location.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    contact_id = Column(Integer, ForeignKey('contact.id'))
    tasks = relationship('Task', secondary=association_table, lazy='subquery',
        backref=db.backref('workpackage', lazy=True))
    
    def total_houres(self):
        pass

    def total_value(self):
        pass

    def get_tasks(self):
        return self.tasks

    @classmethod
    def get_all(cls, user_id):
        return Workpackage.query.filter_by(user_id=user_id).all()