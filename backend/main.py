from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import router as api_v1

app = FastAPI(title='企業級雲盤系統 API', version='3.0.0')
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=['*'], allow_headers=['*'])
app.include_router(api_v1, prefix='/api/v1')

@app.get('/health')
async def health():
    return {'status': 'ok', 'version': '3.0.0'}
