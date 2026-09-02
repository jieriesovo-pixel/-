from fastapi import APIRouter
router = APIRouter()
@router.get('/me')
async def get_me(): return {'username': 'admin'}
@router.get('')
async def list_users(): return []
