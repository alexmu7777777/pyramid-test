from wsgiref.simple_server import make_server

from apps.todo import main
from apps.todo.scripts.initializedb import initialize_db

if __name__ == '__main__':
    initialize_db()
    settings = {}
    app = main(settings)
    server = make_server('127.0.0.1', 8000, app)
    server.serve_forever()
