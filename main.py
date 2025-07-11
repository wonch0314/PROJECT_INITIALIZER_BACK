from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

#CORS origin 정의
origins = [
    "http://127.0.0.1:5173",  # 
    "http://localhost:8000",  # fastapi
]

# .env 파일 로드
load_dotenv()
router = APIRouter(prefix="/api/test", tags=["test"])

@router.get("/")
def test():
    return {"message": "Hello, World!"}

@router.post("/")
def test_post():
    return {"message": "Hello, World!"}

@router.delete("/")
def test_delete():
    return {"message": "Hello, World!"}

@router.put("/")
def test_put():
    return {"message": "Hello, World!"}

def create_app() -> FastAPI:

    # 애플리케이션 설정
    app = FastAPI(
        title="ArchGen API",
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
        description="Architecture Diagram Generator API"
    )
    
    # CORS 설정
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"], 
        #allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Router 설정
    app.include_router(router)
    
    return app

app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 