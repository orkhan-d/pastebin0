from api.db import session, Base, bigint_pk, Mapped, mapped_column

class Note(Base):
    __tablename__ = 'notes'

    id: Mapped[bigint_pk]
    title: Mapped[str] = mapped_column()
    content: Mapped[str] = mapped_column()