from fastapi import APIRouter
from ..dependencies import SessionDep

router = APIRouter(prefix="/schemes", tags=["schemes"])
