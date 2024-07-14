from api.db import session
from .models import Note

async def get_note_by_id(note_id: int) -> Note | None:
    note = await session.get(Note, note_id)
    return note

async def create_note_func(
    title: str, 
    content: str, 
) -> Note:
    note = Note(
        title=title,
        content=content,
    )
    session.add(note)
    await session.commit()
    return note