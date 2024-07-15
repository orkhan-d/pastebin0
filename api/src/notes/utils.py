import base64
from api.db import session
from api.src.notes.exceptions import NoteNotFound
from .models import Note

async def get_note_by_id(note_id: int) -> Note | None:
    note = await session.get(Note, note_id)
    if not note:
        raise NoteNotFound()
    return note

async def get_note_by_hashname(hashname: str) -> Note | None:
    try:
        hashname += '=' * ((4 - len(hashname) % 4) % 4)
        note_id = int(base64.b64decode(hashname).decode())
        return await get_note_by_id(note_id)
    except:
        raise NoteNotFound()

async def generate_hashname(note_id: int) -> str:
    return base64.b64encode(bytes(f"{note_id}", "utf-8")).decode().rstrip('=')

async def create_note_func(
    title: str,
    aws_filename: str
) -> int:
    note = Note(
        title=title,
        aws_filename=aws_filename
    )
    session.add(note)
    await session.commit()
    await session.refresh(note)
    return note.id