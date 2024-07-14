from asyncio import current_task
from sqlalchemy import BIGINT, MetaData

from sqlalchemy.ext.asyncio import AsyncAttrs, create_async_engine, async_sessionmaker, async_scoped_session
from sqlalchemy.orm import sessionmaker, scoped_session, DeclarativeBase, Mapped, mapped_column
import os

from typing import Annotated

engine = create_async_engine(os.environ['DATABASE_URL'])
session = async_scoped_session(async_sessionmaker(bind=engine), current_task)

# constraints naming convention
convention = {
  "ix": "ix_%(column_0_label)s",
  "uq": "uq_%(table_name)s_%(column_0_name)s",
  "ck": "ck_%(table_name)s_%(constraint_name)s",
  "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
  "pk": "pk_%(table_name)s"
}

class Base(AsyncAttrs, DeclarativeBase):
    metadata = MetaData(naming_convention=convention)

# custom types
bigint_pk = Annotated[int, mapped_column(BIGINT, primary_key=True)]