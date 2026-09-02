from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.core.database import get_db
from app.models.file import File as FileModel
from app.storage.factory import get_storage
import uuid

router = APIRouter()

@router.post('/upload/init')
async def init_upload(file_name: str, total_chunks: int):
    return {'upload_id': str(uuid.uuid4()), 'chunk_size': 5242880}

@router.post('/upload/chunk')
async def upload_chunk(upload_id: str=Form(...), chunk_index: int=Form(...),
                       total_chunks: int=Form(...), file_name: str=Form(...),
                       chunk: UploadFile=File(...)):
    data = await chunk.read()
    storage = get_storage()
    await storage.upload(f'temp/{upload_id}/chunk_{chunk_index:05d}', data)
    return {'chunk_index': chunk_index, 'uploaded': True}

@router.post('/upload/complete')
async def complete_upload(upload_id: str=Form(...), file_name: str=Form(...),
                          mime_type: str=Form('application/octet-stream'),
                          folder_id: str=Form(None)):
    return {'id': str(uuid.uuid4()), 'name': file_name, 'message': '上傳完成'}

@router.get('/{file_id}/download')
async def download_file(file_id: str, db: AsyncSession=Depends(get_db)):
    r = await db.execute(select(FileModel).where(FileModel.id == uuid.UUID(file_id)))
    file = r.scalar_one_or_none()
    if not file: raise HTTPException(status_code=404, detail='文件不存在')
    storage = get_storage()
    return StreamingResponse(storage.download_stream(file.storage_key),
                             media_type=file.mime_type or 'application/octet-stream')

@router.delete('/{file_id}')
async def delete_file(file_id: str, db: AsyncSession=Depends(get_db)):
    r = await db.execute(select(FileModel).where(FileModel.id == uuid.UUID(file_id)))
    file = r.scalar_one_or_none()
    if not file: raise HTTPException(status_code=404, detail='文件不存在')
    file.is_deleted = True
    return {'message': '已移至回收站'}
