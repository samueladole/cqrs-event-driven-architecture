from read_side.database.session import engine
from read_side.database.base import Base
from read_side.models import account  # noqa

def init_db():
    Base.metadata.create_all(bind=engine)
