from contextlib import asynccontextmanager
from fastapi import FastAPI
from .dependencies import create_db_and_tables
from .models import user, scheme
from .internal import admin
from .routers import applicants, schemes


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)


app.include_router(applicants.router)
app.include_router(schemes.router)
app.include_router(admin.router, prefix="/admin", tags=["admin"])


@app.get("/")
async def root():
    return {"app_name": "Financial Assistance Scheme Management System"}
