from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
 
# engine = create_engine('sqlite:///test.db')
engine = create_engine( "postgresql://postgres:postgres@localhost:5432/testdb3")

session = Session(
    autocommit = False,
    autoflush = True,
    bind = engine)

Base = declarative_base()
 
class User(Base):
     __tablename__ = 'users'
     id = Column(Integer, primary_key=True)
     name = Column(String)
     password = Column(String)
     fullname = Column(String)
     nickname = Column(String)
 
     def __repr__(self):
        return "<User('name={}', fullname={}, nickname={})>".format(
                      self.name, self.fullname, self.nickname)
 
