from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base
from .base import UUIDMixin, TimestampMixin

class Folder(UUIDMixin, TimestampMixin, Base):
    __tablename__ = 'folders'
    tenant_id = Column(UUID(as_uuid=True), ForeignKey('tenants.id'), nullable=False)
    owner_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    parent_id = Column(UUID(as_uuid=True), ForeignKey('folders.id'), nullable=True)
    name = Column(String(256), nullable=False)
    path = Column(String(2048), nullable=False)
