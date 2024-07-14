from api.db import session
from .models import Note

def get_note(note_id: int) -> Note | None:
    return session.query(Note).filter(Note.id == note_id).first()

def create_note(
    title: str, 
    content: str, 
) -> Note:
    note = Note(
        title=title,
        content=content,
    )
    session.add(note)
    session.commit()
    return note