from sqlmodel import Field, SQLModel


class ApplicationBase(SQLModel):
    applicant_id: int = Field(foreign_key="applicant.id")
    scheme_id: int = Field(foreign_key="scheme.id")


class Application(ApplicationBase, table=True):
    id: int = Field(default=None, primary_key=True)
    status: str = Field(default="pending")


class ApplicationPublic(ApplicationBase):
    id: int
    status: str


class ApplicationCreate(ApplicationBase):
    pass
