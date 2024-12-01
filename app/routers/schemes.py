from fastapi import APIRouter, HTTPException
from sqlmodel import select
from ..dependencies import SessionDep
from ..models.scheme import Scheme, SchemePublic

router = APIRouter(prefix="/schemes", tags=["schemes"])
