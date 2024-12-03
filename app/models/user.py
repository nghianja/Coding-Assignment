from sqlmodel import Field, Relationship, SQLModel
from decimal import Decimal
from enum import Enum


class Gender(Enum):
    MALE = 'male'
    FEMALE = 'female'


class ProfileBase(SQLModel):
    age: int = Field(default=18)
    gender: Gender = Field(default=Gender.MALE)
    salary: Decimal = Field(default=0, decimal_places=2)


class Profile(ProfileBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user: "User" = Relationship(back_populates="profile")


class ProfilePublic(ProfileBase):
    id: int


class ProfileCreate(ProfileBase):
    pass


class ProfileUpdate(SQLModel):
    age: int | None = None
    gender: Gender | None = None
    salary: Decimal | None = None


class UserBase(SQLModel):
    username: str = Field(index=True, unique=True)


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    role: str = Field(index=True)
    password: str
    profile_id: int | None = Field(default=None, foreign_key="profile.id")
    profile: Profile | None = Relationship(back_populates="user")


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
