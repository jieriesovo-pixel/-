from sqlalchemy import Column, String, ForeignKey, JSON, Enum
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base
from .base import UUIDMixin, TimestampMixin
import enum

class AuditAction(str, enum.Enum):
    UPLOAD='upload'; DOWNLOAD='download'; DELETE='delete'
    SHARE='share'; LOGIN='login'; LOGOUT='logout'
    RENAME='rename'; MOVE='move'

class AuditLog(UUIDMixin, TimestampMixin, Base):
    __tablename__ = 'audit_logs'
    tenant_id = Column(UUID(as_uuid=True), ForeignKey('tenants.id'), nullable=False)
    user_id = Column(UUID(as_uuid=True), nullable=True)
    action = Column(Enum(AuditAction), nullable=False)
    resource_id = Column(UUID(as_uuid=True), nullable=True)
    ip_address = Column(String(45), nullable=True)
    details = Column(JSON, default={})
