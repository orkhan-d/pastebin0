from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, DeclarativeBase
import os

engine = create_engine(os.environ['DATABASE_URL'])
session = scoped_session(sessionmaker(bind=engine))

class Base(DeclarativeBase):
    pass