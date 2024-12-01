from contextlib import asynccontextmanager
from fastapi import FastAPI
from passlib.hash import bcrypt
from sqlmodel import select, Session
from .dependencies import create_db_and_tables, engine
from .models.user import User
from .models.scheme import Scheme
from .models.application import Application
from .internal import admin
from .routers import applicants, applications, schemes


def create_root_admin():
    with Session(engine) as session:
        statement = select(User).where(User.role == "admin")
        admin_list = session.exec(statement).all()
        if not admin_list:
            root_admin = User(
                username="root",
                password=bcrypt.hash("RootAdmin"),
                role="admin",
            )
            session.add(root_admin)
            session.commit()
            session.refresh(root_admin)
            print('Created root admin', root_admin)


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    create_root_admin()
    yield


app = FastAPI(lifespan=lifespan)


app.include_router(applications.router)
app.include_router(applicants.router)
app.include_router(schemes.router)
app.include_router(admin.router, prefix="/admin", tags=["admin"])


@app.get("/")
async def root():
    return {"app_name": "Financial Assistance Scheme Management System"}
