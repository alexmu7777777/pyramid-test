from sqlalchemy import engine_from_config, insert
from apps.todo import SQLALCHEMY_URL
from apps.todo.models import Base, User


def initialize_db():
    settings = {'sqlalchemy.url': SQLALCHEMY_URL}
    engine = engine_from_config(settings, prefix='sqlalchemy.')
    if bool(False):  # os.environ.get('DEBUG', '')
        Base.metadata.drop_all(engine)
        insert(User).values(username='alex', email='alex@gmail.com', password="123")
    Base.metadata.create_all(engine)
