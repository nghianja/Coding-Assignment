from fastapi import APIRouter, HTTPException
from passlib.hash import bcrypt
from sqlmodel import select
from ..dependencies import SessionDep
from ..models.user import User, UserPublic, UserCreate, UserUpdate, ApplicantCreate

router = APIRouter(prefix="/applicants", tags=["applicants"])


@router.get("/", response_model=list[UserPublic])
async def read_applicants(session: SessionDep):
    statement = select(User).where(User.role == "applicant")
    applicants = session.exec(statement).all()
    return applicants


@router.get("/{applicant_id}", response_model=UserPublic)
async def read_applicant(applicant_id: int, session: SessionDep):
    applicant = session.get(User, applicant_id)
    if not applicant or applicant.role != "applicant":
        raise HTTPException(status_code=404, detail="Applicant not found")
    return applicant


@router.post("/", response_model=UserPublic)
async def create_applicant(user: UserCreate, session: SessionDep):
    applicant = ApplicantCreate(username=user.username, password=user.password)
    applicant_db = User.model_validate(applicant)
    applicant_db.password = bcrypt.hash(applicant.password)
    session.add(applicant_db)
    session.commit()
    session.refresh(applicant_db)
    return applicant_db


@router.patch("/{applicant_id}", response_model=UserPublic)
async def update_applicant(applicant_id: int, applicant: UserUpdate, session: SessionDep):
    applicant_db = session.get(User, applicant_id)
    if not applicant_db or applicant_db.role != "applicant":
        raise HTTPException(status_code=404, detail="Applicant not found")
    if applicant.password != None:
        applicant.password = bcrypt.hash(applicant.password)
    applicant_data = applicant.model_dump(exclude_unset=True)
    print(applicant_data)
    applicant_db.sqlmodel_update(applicant_data)
    session.add(applicant_db)
    session.commit()
    session.refresh(applicant_db)
    return applicant_db


@router.delete("/{applicant_id}")
async def delete_applicant(applicant_id: int, session: SessionDep):
    applicant = session.get(User, applicant_id)
    if not applicant or applicant.role != "applicant":
        raise HTTPException(status_code=404, detail="Applicant not found")
    session.delete(applicant)
    session.commit()
    return {"ok": True}
