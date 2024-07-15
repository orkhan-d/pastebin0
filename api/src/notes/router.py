from typing import Annotated
from uuid import uuid4
from fastapi import APIRouter, Depends, status, File
from fastapi.responses import JSONResponse

from api.deps import get_s3_client
from api.s3 import S3Bucket

from .models import Note
from api.utils import sqlalchemy_to_pydantic
from .schemas import CreateNoteSchema, NoteInfoSchema
from .utils import get_note_by_id, create_note_func

router = APIRouter(prefix='/notes', tags=['notes'])

@router.get('/{note_id}')
async def read_notes(note: Annotated[Note, Depends(get_note_by_id)],
                     s3: Annotated[S3Bucket, Depends(get_s3_client)]):
    content = await s3.get_file(note.aws_filename)
    data = NoteInfoSchema(title=note.title, content=content.decode())

    return JSONResponse(data.model_dump(), status.HTTP_200_OK)

@router.post('/')
async def create_note(note: CreateNoteSchema,
                      s3: Annotated[S3Bucket, Depends(get_s3_client)]):
    
    aws_filename = f'{uuid4()}.txt'
    await s3.upload_file(aws_filename, note.content.encode())
    await create_note_func(note.title, aws_filename)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={'message': 'Note created successfully'}
    )