from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
import zope.sqlalchemy

SQLALCHEMY_URL = 'sqlite:////home/alexmu/PycharmProjects/todos/todos.db'  # os.environ.get('DATABASE_URL', '')


def get_session_factory(engine):
    """Return a generator of database session objects."""
    factory = sessionmaker()
    factory.configure(bind=engine)
    return factory


def get_tm_session(session_factory, transaction_manager):
    """Build a session and register it as a transaction-managed session."""
    dbsession = session_factory()
    zope.sqlalchemy.register(dbsession, transaction_manager=transaction_manager)
    return dbsession


def main(global_config, **settings):
    """Returns a Pyramid WSGI application."""
    settings['sqlalchemy.url'] = SQLALCHEMY_URL
    settings['tm.manager_hook'] = 'pyramid_tm.explicit_manager'
    config = Configurator(settings=settings)
    config.include('.routes')
    config.include('pyramid_tm')
    config.include('pyramid_mako')
    config.add_mako_renderer('.html')
    session_factory = get_session_factory(engine_from_config(settings, prefix='sqlalchemy.'))
    config.registry['dbsession_factory'] = session_factory
    config.add_request_method(
        lambda request: get_tm_session(session_factory, request.tm),
        'dbsession',
        reify=True
    )

    config.scan()
    return config.make_wsgi_app()
