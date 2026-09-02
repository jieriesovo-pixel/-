from fastapi import APIRouter
from .auth import router as auth_router
from .files import router as files_router
from .folders import router as folders_router
from .search import router as search_router
from .share import router as share_router
from .users import router as users_router
from .admin import router as admin_router
from .audit import router as audit_router

router = APIRouter()
router.include_router(auth_router, prefix='/auth', tags=['認證'])
router.include_router(files_router, prefix='/files', tags=['文件'])
router.include_router(folders_router, prefix='/folders', tags=['文件夾'])
router.include_router(search_router, prefix='/search', tags=['搜索'])
router.include_router(share_router, prefix='/shares', tags=['分享'])
router.include_router(users_router, prefix='/users', tags=['用戶'])
router.include_router(admin_router, prefix='/admin', tags=['管理'])
router.include_router(audit_router, prefix='/audit', tags=['審計'])
