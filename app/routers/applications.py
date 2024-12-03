from fastapi import APIRouter, HTTPException
from sqlmodel import select
from ..dependencies import SessionDep
from ..models.application import Application, ApplicationPublic, ApplicationCreate
from ..models.user import User

router = APIRouter(prefix="/applications", tags=["applications"])


@router.get("/", response_model=list[ApplicationPublic])
async def read_applications(session: SessionDep, applicant_id: int | None = None):
    statement = select(Application)
    if applicant_id:
        applicant = session.get(User, applicant_id)
        if not applicant or applicant.role != "applicant":
            raise HTTPException(status_code=404, detail="Applicant not found")
        statement = statement.where(Application.applicant_id == applicant_id)
    applications = session.exec(statement).all()
    return applications


@router.get("/{application_id}", response_model=ApplicationPublic)
async def read_application(session: SessionDep, application_id: int):
    application = session.get(Application, application_id)
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    return application


@router.post("/", response_model=ApplicationPublic)
async def create_application(session: SessionDep, application: ApplicationCreate):
    application_db = Application.model_validate(application)
    session.add(application_db)
    session.commit()
    session.refresh(application_db)
    return application_db


@router.delete("/{application_id}")
async def delete_application(session: SessionDep, application_id: int):
    application = session.get(Application, application_id)
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    session.delete(application)
    session.commit()
    return {"ok": True}


@router.patch("/{application_id}/status/approved", response_model=ApplicationPublic)
async def approve_application(session: SessionDep, application_id: int):
    application = session.get(Application, application_id)
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    application.status = "approved"
    session.add(application)
    session.commit()
    session.refresh(application)
    return application


@router.patch("/{application_id}/status/rejected", response_model=ApplicationPublic)
async def reject_application(session: SessionDep, application_id: int):
    application = session.get(Application, application_id)
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    application.status = "rejected"
    session.add(application)
    session.commit()
    session.refresh(application)
    return application
