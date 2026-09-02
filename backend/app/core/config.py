from pydantic_settings import BaseSettings
from typing import List
import secrets

class Settings(BaseSettings):
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440
    ALGORITHM: str = 'HS256'
    DATABASE_URL: str = 'postgresql+asyncpg://clouddrive:clouddrive@postgres:5432/clouddrive'
    REDIS_URL: str = 'redis://redis:6379/0'
    ES_URL: str = 'http://elasticsearch:9200'
    ES_INDEX_FILES: str = 'clouddrive_files'
    STORAGE_BACKEND: str = 'local'
    STORAGE_LOCAL_PATH: str = '/data/storage'
    CHUNK_SIZE: int = 5242880
    class Config:
        env_file = '.env'

settings = Settings()
