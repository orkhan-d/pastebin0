from fastapi import APIRouter

router = APIRouter(prefix='/notes', tags=['notes'])

@router.get('/')
async def read_notes():
    return 