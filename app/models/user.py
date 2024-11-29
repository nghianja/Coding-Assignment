from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    name: str = Field(index=True)
    role: str = Field(index=True)


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    password: str


class UserPublic(UserBase):
    id: int


class UserCreate(UserBase):
    password: str


class UserUpdate(SQLModel):
    name: str | None = None
    role: str | None = None
    password: str | None = None
