from sqlalchemy import Column, String, BigInteger, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base
from .base import UUIDMixin, TimestampMixin

class File(UUIDMixin, TimestampMixin, Base):
    __tablename__ = 'files'
    tenant_id = Column(UUID(as_uuid=True), ForeignKey('tenants.id'), nullable=False)
    owner_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    folder_id = Column(UUID(as_uuid=True), ForeignKey('folders.id'), nullable=True)
    name = Column(String(512), nullable=False)
    original_name = Column(String(512), nullable=False)
    mime_type = Column(String(128))
    size = Column(BigInteger, default=0)
    storage_key = Column(String(1024), nullable=False)
    content_hash = Column(String(64), index=True)
    version = Column(Integer, default=1)

class FileVersion(UUIDMixin, TimestampMixin, Base):
    __tablename__ = 'file_versions'
    file_id = Column(UUID(as_uuid=True), ForeignKey('files.id'), nullable=False)
    version = Column(Integer, nullable=False)
    storage_key = Column(String(1024), nullable=False)
    size = Column(BigInteger, default=0)
    uploader_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
