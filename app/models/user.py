from sqlmodel import Field, Relationship, SQLModel
from decimal import Decimal
from .enums import Gender, Role


class ProfileBase(SQLModel):
    age: int = Field(default=18)
    # gender: Gender = Field(default=Gender.MALE)
    gender: str = Field(default="both")
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
    gender: str | None = None
    salary: Decimal | None = None


class UserBase(SQLModel):
    username: str = Field(index=True, unique=True)


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    # role: Role = Field(default=Role.GUEST)
    role: str = Field(default="guest")
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
    # role: Role = Role.ADMIN
    role: str = "admin"


class ApplicantCreate(UserCreate):
    # role: Role = Role.APPLICANT
    role: str = "applicant"
