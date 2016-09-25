# -*- coding:utf-8 -*-


from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Sequence
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import ConfigParser


def db_init(config):
    conf = ConfigParser.ConfigParser()
    conf.read(config)
    db = conf.get('defaults', 'db')

    return db


db = db_init('db.conf')

Engine = create_engine(db, echo=False)

Session = sessionmaker(bind=Engine)

Base = declarative_base()



class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    numbers = Column(Integer)
    email = Column(String(120))
    address = Column(String(120))
    phonenumber = Column(String(11), index=True, unique=True)
    money = Column(String(12))

session = Session()
Base.metadata.create_all(Engine)
session.commit()
if __name__ == "__main__":

    # session = Session()
    new_user = User(name="cz", numbers=10, email="chenze@126.com", address="sjz", phonenumber="18411031619",
                    money="333")
    session.add(new_user)

    session.query(User).filter(User.id == 1).update({User.name:"cz",User.phonenumber:"1234567899"})
    session.commit()
#    print session.query(User.name).filter(User.id > 1, User.id < 3).all()
