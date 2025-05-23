from fastapi import FastAPI
import uvicorn

from auth.auth import auth_backend,fastapi_users
from auth.schemas import UserCreate,UserRead

from fastapi.middleware.cors import CORSMiddleware

from api.user_route import router as user_router
from api.cancer_route import router as cancer_router
from api.news_route import router as news_router



app = FastAPI(
    title='NSCheck',
)



origins = [
    "http://127.0.0.1:5173",
    "http://127.0.0.1",
    "http://localhost",
    "http://localhost:5173",
    "http://localhost:5173/",
    "http://213.171.15.163",
    "http://213.171.15.163/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)






@app.get("/")
async def home():
    return "Hello World"



app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)


app.include_router(user_router)
app.include_router(cancer_router)
app.include_router(news_router)



