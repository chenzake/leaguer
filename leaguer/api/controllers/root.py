from pecan import rest
from wsme import types as wtypes
import wsmeext.pecan as wsme_pecan
from leaguer.api import expose
from leaguer.api.controllers.v1 import controller as v1


class RootController(rest.RestController):

    v1 = v1.V1Controller()

    @expose.expose(wtypes.text)
    def get(self):
        return "hello world!"
