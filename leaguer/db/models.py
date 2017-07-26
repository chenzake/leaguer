from sqlalchemy import Column, String, Integer, Sequence
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
    money = Column(String(12))

    def as_dict(self):
        d = {}
        for c in self.__table__.columns:
            d[c.name] = self[c.name]
        return d
    