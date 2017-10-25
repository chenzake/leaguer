# -*- coding:utf-8 -*-

from sqlalchemy import BigInteger
from sqlalchemy import Float,Date, DateTime
from sqlalchemy import Column, String, Integer, Sequence
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
#     __table_args__ = (
#         Index('ix_user_user_id', 'name'),
#     )
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50),)
    numbers = Column(Integer)
    email = Column(String(120))
    address = Column(String(120))
    phonenumber = Column(String(11), index=True, unique=True)

    def as_dict(self):
        d = {}
        for c in self.__table__.columns:
            d[c.name] = self[c.name]
        return d


class Wares(Base):

    __tablename__ = 'wares'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(50),)
    cost = Column(Float)
    price = Column(Float)
    preferential_price = Column(Float)
    num = Column(Integer)
    create_time = Column(Date)

    def __init__(self, id=None, name=None, cost=None, price=None,
                 preferential_price=None, num=None, create_time=None):
        self.id = self.__class__.id = id
        self.name = self.__class__.name = name
        self.cost = self.__class__.cost = cost
        self.price = self.__class__.price = price
        self.preferential_price = \
            self.__class__.preferential_price = preferential_price
        self.num = self.__class__.num = num
        self.create_time = self.__class__.create_time =create_time


class Sold_Note(Base):

    __tablename__ = 'sold_note'
    sold_id = Column(BigInteger, ForeignKey('wares.id'), index=True)
    sold_name = Column(String(50))
    sold_time = Column(DateTime, index=True)
    sold_num = Column(Integer)
    unit_price = Column(Float)
    total_cost = Column(Float)
    total_price = Column(Float)


class Profits(Base):

    __tablename__ = 'profits'
    date = Column(Date)
    price = Column(Float)
    cost = Column(Float)
    profit = Column(Float)