from pecan import rest
from wsme import types as wtypes
import wsmeext.pecan as wsme_pecan
from pecan import expose

class RootController(rest.RestController):

    #@wsme_pecan.wsexpose(wtypes.text)
    @expose('json')
    def get(self):
        return "hello world!"
