from pydantic import BaseModel

class CreateNoteSchema(BaseModel):
    title: str
    content: str

class NoteInfoSchema(BaseModel):
    title: str
    content: str