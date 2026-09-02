from fastapi import APIRouter, Query
router = APIRouter()
@router.get('')
async def list_audit_logs(page: int=Query(1), size: int=Query(50)):
    return []
