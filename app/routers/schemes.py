from fastapi import APIRouter, HTTPException
from sqlmodel import or_, select
from ..dependencies import SessionDep
from ..models.scheme import Scheme, SchemePublic, SchemeCreate, SchemeUpdate
from ..models.user import User

router = APIRouter(prefix="/schemes", tags=["schemes"])


@router.get("/", response_model=list[SchemePublic])
async def read_schemes(session: SessionDep, applicant_id: int | None = None):
    statement = select(Scheme)
    if applicant_id:
        applicant = session.get(User, applicant_id)
        if not applicant or applicant.role != "applicant":
            raise HTTPException(status_code=404, detail="Applicant not found")
        if applicant.profile is None:
            raise HTTPException(status_code=404, detail="Profile not found")
        statement = statement.where(Scheme.minimum_age <= applicant.profile.age)
        statement = statement.where(Scheme.maximum_salary >= applicant.profile.salary)
        statement = statement.where(or_(Scheme.suitable_gender == "both", Scheme.suitable_gender == applicant.profile.gender))
    schemes = session.exec(statement).all()
    return schemes


@router.get("/{scheme_id}", response_model=SchemePublic)
async def read_scheme(scheme_id: int, session: SessionDep):
    scheme = session.get(Scheme, scheme_id)
    if not scheme:
        raise HTTPException(status_code=404, detail="Scheme not found")
    return scheme


@router.post("/", response_model=SchemePublic)
async def create_scheme(scheme: SchemeCreate, session: SessionDep):
    scheme_db = Scheme.model_validate(scheme)
    session.add(scheme_db)
    session.commit()
    session.refresh(scheme_db)
    return scheme_db


@router.patch("/{scheme_id}", response_model=SchemePublic)
async def update_scheme(scheme_id: int, scheme: SchemeUpdate, session: SessionDep):
    scheme_db = session.get(Scheme, scheme_id)
    if not scheme_db:
        raise HTTPException(status_code=404, detail="Scheme not found")
    scheme_data = scheme.model_dump(exclude_unset=True)
    scheme_db.sqlmodel_update(scheme_data)
    session.add(scheme_db)
    session.commit()
    session.refresh(scheme_db)
    return scheme_db


@router.delete("/{scheme_id}")
async def delete_scheme(scheme_id: int, session: SessionDep):
    scheme = session.get(Scheme, scheme_id)
    if not scheme:
        raise HTTPException(status_code=404, detail="Scheme not found")
    session.delete(scheme)
    session.commit()
    return {"ok": True}
