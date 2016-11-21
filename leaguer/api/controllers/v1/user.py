# -*- coding: utf-8 -*-

import pecan
from pecan import rest
from wsme import types as wtypes
from leaguer.api import expose
from leaguer.db import session
from leaguer.db import User as db_user


class User(wtypes.Base):
    uuid = wtypes.UuidType()
    id = uuid
    name = wtypes.text
    numbers = wtypes.text
    email = wtypes.text
    address = wtypes.text
    phonenumbers = wtypes.text
    money = wtypes.text


class UserController(rest.RestController):

    def __init__(self, user_id):
        self.user_id = int(user_id)

    @expose.expose(User)
    def get(self):
        user = session.query(db_user).filter_by(id=self.user_id).one()
        return User(**user.as_dict())


class Users(wtypes.Base):
    users = [User]


class UsersController(rest.RestController):

    @expose.expose(Users)
    def get(self):
        users = session.query(db_user).all()
        user_list = []
        for user in users:
            u = User()
            u.id = user.id
            u.name = user.name
            u.numbers = user.number
            u.email = user.email
            u.address = user.address
            u.phonenumbers = user.phonenumbers
            u.money = user.money
            user_list.append(u)
        return Users(users=user_list)

    @pecan.expose()
    def _lookup(self, user_id, *remainder):
        return UserController(user_id), remainder


