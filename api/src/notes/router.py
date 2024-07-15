from typing import Annotated
from uuid import uuid4
from fastapi import APIRouter, Depends, status, File
from fastapi.responses import JSONResponse

from api.deps import get_s3_client
from api.s3 import S3Bucket

from .models import Note
from .schemas import CreateNoteSchema, NoteInfoSchema
from .utils import generate_hashname, get_note_by_hashname, create_note_func

router = APIRouter(prefix='/notes', tags=['notes'])

@router.get('/{hashname}')
async def read_notes(note: Annotated[Note, Depends(get_note_by_hashname)],
                     s3: Annotated[S3Bucket, Depends(get_s3_client)]):
    try:
        content = await s3.get_file(note.aws_filename)
        data = NoteInfoSchema(title=note.title, content=content.decode())

        return JSONResponse(data.model_dump(), status.HTTP_200_OK)
    except:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={'message': 'Note not found'}
        )

@router.post('/')
async def create_note(data: CreateNoteSchema,
                      s3: Annotated[S3Bucket, Depends(get_s3_client)]):
    aws_filename = f'{uuid4()}.txt'
    await s3.upload_file(aws_filename, data.content.encode())
    note_id = await create_note_func(data.title, aws_filename)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            'message': 'Note created successfully',
            'hashname': await generate_hashname(note_id)
        }
    )