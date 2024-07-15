from api.db import session
from .models import Note

async def get_note_by_id(note_id: int) -> Note | None:
    note = await session.get(Note, note_id)
    return note

async def create_note_func(
    title: str,
    aws_filename: str
) -> Note:
    note = Note(
        title=title,
        aws_filename=aws_filename
    )
    session.add(note)
    await session.commit()
    return note