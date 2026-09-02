from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.models.user import User
from app.core.security import verify_password, decode_token
from app.core.database import get_db
from jose import JWTError
import uuid

bearer = HTTPBearer()

async def get_current_user(
    creds: HTTPAuthorizationCredentials = Depends(bearer),
    db: AsyncSession = Depends(get_db)
) -> User:
    try:
        payload = decode_token(creds.credentials)
        user_id = payload.get('sub')
    except JWTError:
        raise HTTPException(status_code=401, detail='令牌無效')
    r = await db.execute(select(User).where(User.id == uuid.UUID(user_id), User.is_deleted == False))
    user = r.scalar_one_or_none()
    if not user: raise HTTPException(status_code=401, detail='用戶不存在')
    return user
