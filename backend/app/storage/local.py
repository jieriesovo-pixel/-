import aiofiles
from pathlib import Path
from typing import AsyncIterator
from .base import StorageBackend
from app.core.config import settings

class LocalStorage(StorageBackend):
    def __init__(self):
        self.base = Path(settings.STORAGE_LOCAL_PATH)
        self.base.mkdir(parents=True, exist_ok=True)
    def _p(self, key):
        p = self.base / key; p.parent.mkdir(parents=True, exist_ok=True); return p
    async def upload(self, key, data, content_type=''):
        async with aiofiles.open(self._p(key), 'wb') as f: await f.write(data)
        return key
    async def download(self, key):
        async with aiofiles.open(self._p(key), 'rb') as f: return await f.read()
    async def download_stream(self, key) -> AsyncIterator[bytes]:
        async with aiofiles.open(self._p(key), 'rb') as f:
            while chunk := await f.read(settings.CHUNK_SIZE): yield chunk
    async def delete(self, key):
        p = self._p(key)
        if p.exists(): p.unlink(); return True
        return False
    async def get_url(self, key, expires=3600): return f'/api/v1/files/{key}/download'
    async def copy(self, src, dst):
        import shutil; shutil.copy2(self._p(src), self._p(dst)); return dst
