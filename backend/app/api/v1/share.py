from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.core.database import get_db
from app.models.share import ShareLink
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import secrets

router = APIRouter()

class ShareCreate(BaseModel):
    file_id: str
    expires_at: Optional[datetime] = None
    password: Optional[str] = None
    allow_download: bool = True
    allow_preview: bool = True

@router.post('')
async def create_share(body: ShareCreate):
    return {'token': secrets.token_urlsafe(32), 'is_active': True, 'download_count': 0}

@router.post('/{token}/access')
async def access_share(token: str, db: AsyncSession=Depends(get_db)):
    r = await db.execute(select(ShareLink).where(ShareLink.token==token, ShareLink.is_active==True))
    share = r.scalar_one_or_none()
    if not share: raise HTTPException(404, '外鏈不存在')
    return {'allow_download': share.allow_download, 'allow_preview': share.allow_preview}

@router.get('/my')
async def my_shares():
    return []
