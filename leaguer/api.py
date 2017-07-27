from wsgiref import simple_server
from leaguer.api import app


def main():
    host = '0.0.0.0'
    port = 8900

    application = app.setup_app()
    server = simple_server.make_server(host, port, application)
    server.serve_forever()

main()
