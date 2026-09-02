from sqlalchemy.ext.asyncio import AsyncSession
from app.models.audit import AuditLog

class AuditService:
    async def log(self, db: AsyncSession, **kwargs):
        entry = AuditLog(**kwargs); db.add(entry); await db.flush(); return entry

audit_service = AuditService()
