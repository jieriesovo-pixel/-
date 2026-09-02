from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from pydantic import BaseModel
from typing import Optional
import uuid

router = APIRouter()

class FolderCreate(BaseModel):
    name: str
    parent_id: Optional[str] = None

@router.get('')
async def list_folders(parent_id: Optional[str]=None):
    return {'folders': [], 'files': []}

@router.post('')
async def create_folder(body: FolderCreate):
    return {'id': str(uuid.uuid4()), 'name': body.name}
