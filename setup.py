from setuptools import setup

requires = [
    'pyramid',
    'pyramid-mako',
    'sqlalchemy',
    'deform',
    'colander',
    'pyramid_tm',  # allows Pyramid requests to join the active transaction as provided by the transaction package.
    'transaction',  # generic transaction implementation for Python. It is mainly used by the ZODB.
    'zope.sqlalchemy',  # unite existing packages integrating SQLAlchemy with Zope’s transaction management.
    'pyramid_chameleon',
]

setup(
    entry_points={
        'paste.app_factory': [
            'main = todo:main',
        ],
        'console_scripts': [
            'initdb = todo.scripts.initializedb:main',
        ],
    }
)

# requires = [
#     'pyramid',
#     'pyramid-ipython',
#     'waitress',
#     'sqlalchemy',
#     'psycopg2',
#     'pyramid_tm',
#     'transaction',
#     'zope.sqlalchemy'
# ]
