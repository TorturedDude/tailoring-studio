from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from models.database import engine, Base
from routers.master_router import router as master_router
from routers.user_router import router as user_router
from routers.review_router import router as review_router
from routers.order_router import router as order_router
from routers.clothingmodel_router import router as clothingmodel_router

app = FastAPI()

# templates = Jinja2Templates(directory="templates")
# app.mount("/static", StaticFiles(directory="static"), name="static")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

app.include_router(user_router, tags=['Users'])
app.include_router(master_router, tags=['Masters'])
app.include_router(review_router, tags=['Reviews'])
app.include_router(order_router, tags=['Orders'])
app.include_router(clothingmodel_router, tags=['Clothes'])

Base.metadata.create_all(bind=engine)