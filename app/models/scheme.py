from sqlmodel import Field, SQLModel
from decimal import Decimal
from .enums import Gender


class SchemeBase(SQLModel):
    name: str = Field(index=True, unique=True)
    description: str
    minimum_age: int = Field(default=18)
    maximum_salary: Decimal = Field(default=0, decimal_places=2)
    # suitable_gender: Gender = Field(default=Gender.BOTH)
    suitable_gender: str = Field(default="both")


class Scheme(SchemeBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class SchemePublic(SchemeBase):
    id: int


class SchemeCreate(SchemeBase):
    pass


class SchemeUpdate(SchemeBase):
    name: str | None = None
    description: str | None = None
    minimum_age: int | None = None
    maximum_salary: Decimal | None = None
