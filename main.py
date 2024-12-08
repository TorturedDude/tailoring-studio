from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from models.database import engine, Base
from routers.user_router import router as user_router

app = FastAPI()

# templates = Jinja2Templates(directory="templates")
# app.mount("/static", StaticFiles(directory="static"), name="static")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

app.include_router(user_router, tags=['Users'])

Base.metadata.create_all(bind=engine)