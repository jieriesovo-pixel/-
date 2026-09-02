from functools import lru_cache
from app.core.config import settings

@lru_cache(maxsize=1)
def get_storage():
    b = settings.STORAGE_BACKEND.lower()
    if b == 's3':
        from .s3 import S3Storage; return S3Storage()
    from .local import LocalStorage; return LocalStorage()
