from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from read_side.settings import settings

engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False},
    future=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)
