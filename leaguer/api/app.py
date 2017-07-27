import pecan

from leaguer.api import config 
from leaguer.api import hooks


def get_config():
    filename = config.__file__.replace('.pyc', '.py')
    return pecan.configuration.conf_from_file(filename)


def setup_app():

    app_config = get_config()
    
    app_hooks = [hooks.DBHook()]

    app_conf = dict(app_config.app)
    
    app = pecan.make_app(
        app_conf.pop('root'),
        logging=getattr(app_config, 'logging', {}),
        hooks=app_hooks,
        **app_conf
        )
    return app
