from sqlmodel import Field, SQLModel


class SchemeBase(SQLModel):
    name: str = Field(index=True, unique=True)
    description: str


class Scheme(SchemeBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class SchemePublic(SchemeBase):
    id: int


class SchemeCreate(SchemeBase):
    pass


class SchemeUpdate(SchemeBase):
    name: str | None = None
    description: str | None = None
