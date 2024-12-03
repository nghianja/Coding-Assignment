from sqlmodel import Field, SQLModel
from decimal import Decimal


class UserBase(SQLModel):
    username: str = Field(index=True, unique=True)
    details_id: int | None = Field(default=None, foreign_key="userdetails.id")


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    role: str = Field(index=True)
    password: str


class UserPublic(UserBase):
    id: int


class UserCreate(UserBase):
    password: str


class UserUpdate(SQLModel):
    username: str | None = None
    password: str | None = None


class AdminCreate(UserCreate):
    role: str = "admin"


class ApplicantCreate(UserCreate):
    role: str = "applicant"


class UserDetailsBase(SQLModel):
    age: int | None = Field(default=None)
    gender: str | None
    salary: Decimal | None = Field(default=None, decimal_places=2)


class UserDetails(UserDetailsBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
