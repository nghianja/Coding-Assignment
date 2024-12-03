from sqlmodel import Enum


class Gender(Enum):
    MALE = 'male'
    FEMALE = 'female'
    BOTH = 'both'


class Role(Enum):
    ADMIN = 'admin'
    APPLICANT = 'applicant'
    GUEST = 'guest'
