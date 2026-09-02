from sqlalchemy import Column, String, Boolean, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
import enum
from app.core.database import Base
from .base import UUIDMixin, TimestampMixin

class UserRole(str, enum.Enum):
    SUPER_ADMIN = 'super_admin'
    TENANT_ADMIN = 'tenant_admin'
    MEMBER = 'member'
    VIEWER = 'viewer'

class User(UUIDMixin, TimestampMixin, Base):
    __tablename__ = 'users'
    tenant_id = Column(UUID(as_uuid=True), ForeignKey('tenants.id'), nullable=False)
    email = Column(String(256), nullable=False, unique=True, index=True)
    username = Column(String(64), nullable=False)
    hashed_password = Column(String(256), nullable=False)
    role = Column(Enum(UserRole), default=UserRole.MEMBER)
    is_active = Column(Boolean, default=True)
