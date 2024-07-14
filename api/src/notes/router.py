from typing import Annotated
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from .schemas import CreateNoteSchema, NoteInfoSchema
from .utils import get_note_by_id, create_note_func

router = APIRouter(prefix='/notes', tags=['notes'])

@router.get('/{note_id}')
async def read_notes(note: Annotated[NoteInfoSchema, Depends(get_note_by_id)]):
    return note

@router.post('/')
async def create_note(note: CreateNoteSchema):
    await create_note_func(note.title, note.content)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={'message': 'Note created successfully'}
    )