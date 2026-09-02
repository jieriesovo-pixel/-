from sqlalchemy import Column, String, Integer, Boolean
from app.core.database import Base
from .base import UUIDMixin, TimestampMixin

class Tenant(UUIDMixin, TimestampMixin, Base):
    __tablename__ = 'tenants'
    name = Column(String(128), nullable=False, unique=True)
    slug = Column(String(64), nullable=False, unique=True, index=True)
    storage_quota = Column(Integer, default=10737418240)
    storage_used = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)
