from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.core.database import get_db
from app.core.security import create_access_token, verify_password
from app.models.user import User
from pydantic import BaseModel

router = APIRouter()

class LoginReq(BaseModel):
    email: str
    password: str

@router.post('/login')
async def login(body: LoginReq, db: AsyncSession = Depends(get_db)):
    r = await db.execute(select(User).where(User.email == body.email, User.is_deleted == False))
    user = r.scalar_one_or_none()
    if not user or not verify_password(body.password, user.hashed_password):
        raise HTTPException(status_code=401, detail='憑證無效')
    return {'access_token': create_access_token(str(user.id)), 'token_type': 'bearer',
            'user_id': str(user.id), 'username': user.username,
            'role': user.role.value, 'tenant_id': str(user.tenant_id)}

@router.post('/logout')
async def logout():
    return {'message': '已登出'}
