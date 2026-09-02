from abc import ABC, abstractmethod
from typing import AsyncIterator

class StorageBackend(ABC):
    @abstractmethod
    async def upload(self, key, data, content_type=''): pass
    @abstractmethod
    async def download(self, key): pass
    @abstractmethod
    async def download_stream(self, key) -> AsyncIterator[bytes]: pass
    @abstractmethod
    async def delete(self, key): pass
    @abstractmethod
    async def get_url(self, key, expires=3600): pass
    @abstractmethod
    async def copy(self, src, dst): pass
