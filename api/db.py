from sqlalchemy import create_engine, BIGINT, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session, DeclarativeBase, Mapped, mapped_column
import os

from typing import Annotated

engine = create_engine(os.environ['DATABASE_URL'])
session = scoped_session(sessionmaker(bind=engine))

# constraints naming convention
convention = {
  "ix": "ix_%(column_0_label)s",
  "uq": "uq_%(table_name)s_%(column_0_name)s",
  "ck": "ck_%(table_name)s_%(constraint_name)s",
  "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
  "pk": "pk_%(table_name)s"
}

class Base(DeclarativeBase):
    metadata = MetaData(naming_convention=convention)

# custom types
bigint_pk = Annotated[int, mapped_column(BIGINT, primary_key=True)]