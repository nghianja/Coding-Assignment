from fastapi import APIRouter
from ..dependencies import SessionDep

router = APIRouter(prefix="/applicants", tags=["applicants"])
