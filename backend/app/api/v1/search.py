from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional, List

router = APIRouter()

class SearchReq(BaseModel):
    query: str
    page: int = 1
    size: int = 20

@router.post('')
async def search(body: SearchReq):
    return {'total': 0, 'items': []}
