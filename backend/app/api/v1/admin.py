from fastapi import APIRouter
router = APIRouter()
@router.get('/dashboard')
async def dashboard():
    return {'user_count': 0, 'file_count': 0, 'storage_used': 0, 'storage_quota': 107374182400}
