import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID

class TimestampMixin:
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    is_deleted = Column(Boolean, default=False)

class UUIDMixin:
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
