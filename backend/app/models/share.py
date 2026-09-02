from sqlalchemy import Column, String, ForeignKey, DateTime, Boolean, Integer
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base
from .base import UUIDMixin, TimestampMixin

class ShareLink(UUIDMixin, TimestampMixin, Base):
    __tablename__ = 'share_links'
    tenant_id = Column(UUID(as_uuid=True), ForeignKey('tenants.id'), nullable=False)
    file_id = Column(UUID(as_uuid=True), ForeignKey('files.id'), nullable=False)
    creator_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    token = Column(String(64), unique=True, nullable=False, index=True)
    expires_at = Column(DateTime(timezone=True), nullable=True)
    password_hash = Column(String(256), nullable=True)
    download_limit = Column(Integer, nullable=True)
    download_count = Column(Integer, default=0)
    allow_preview = Column(Boolean, default=True)
    allow_download = Column(Boolean, default=True)
    is_active = Column(Boolean, default=True)
