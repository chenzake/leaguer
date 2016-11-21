# -*- coding: utf-8 -*-

from pecan import rest
from wsme import types as wtypes
from leaguer.api import expose
from leaguer.api.controllers.v1 import user


class V1Controller(rest.RestController):

    user = user.UsersController()

    @expose.expose(wtypes.text)
    def get(self):
        return "v1 version"
