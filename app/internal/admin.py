from fastapi import APIRouter, HTTPException
from sqlmodel import select
from ..dependencies import SessionDep
from ..models.scheme import Scheme, SchemePublic
from ..models.user import User, UserPublic, UserCreate, UserUpdate

router = APIRouter()


@router.get("/", response_model=list[UserPublic])
async def read_admins(session: SessionDep):
    statement = select(User).where(User.role == "admin")
    admins = session.exec(statement).all()
    return admins


@router.get("/{admin_id}", response_model=UserPublic)
async def read_admin(admin_id: int, session: SessionDep):
    admin = session.get(User, admin_id)
    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found")
    return admin


@router.post("/", response_model=UserPublic)
async def create_admin(admin: UserCreate, session: SessionDep):
    admin_db = User.model_validate(admin)
    session.add(admin_db)
    session.commit()
    session.refresh(admin_db)
    return admin_db


@router.patch("/{admin_id}", response_model=UserPublic)
async def update_admin(admin_id: int, admin: UserUpdate, session: SessionDep):
    admin_db = session.get(User, admin_id)
    if not admin_db:
        raise HTTPException(status_code=404, detail="Admin not found")
    admin_data = admin.model_dump(exclude_unset=True)
    admin_db.sqlmodel_update(admin_data)
    session.add(admin_db)
    session.commit()
    session.refresh(admin_db)
    return admin_db


@router.delete("/{admin_id}")
async def delete_admin(admin_id: int, session: SessionDep):
    admin = session.get(User, admin_id)
    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found")
    session.delete(admin)
    session.commit()
    return {"ok": True}
