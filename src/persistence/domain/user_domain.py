from sqlalchemy import Column, String, Integer

from src.persistence.domain import BaseDomain
from src.usecases.entity.user import UserEntity


class UserDomain(BaseDomain):
    __tablename__ = 'user'

    name = Column(String(50), nullable=False, index=False)
    surname = Column(String(50), nullable=False, index=True)
    cpf = Column(String(11), unique=True, nullable=False, index=True)
    age = Column(Integer, nullable=False, index=False)
    email = Column(String(50), unique=True, nullable=False, index=True)
    cellphone = Column(String(13), unique=True, nullable=False, index=True)

    @property
    def to_entity(self) -> UserEntity:
        return UserEntity(
            id=self.id,
            name=self.name,
            surname=self.surname,
            age=self.age,
            cpf=self.cpf,
            email=self.email,
            cellphone=self.cellphone,
            available=self.available
        )

    FIELDS = {
        'name': str,
        'surname': str,
        'age': int,
        'cpf': str,
        'email': str,
        'cellphone': str
    }

    FIELDS.update(BaseDomain.FIELDS)


def to_domain(user_entity: UserEntity) -> UserDomain:
    return UserDomain(
        id=user_entity.id,
        name=user_entity.name,
        surname=user_entity.surname,
        cpf=user_entity.cpf,
        age=user_entity.age,
        email=user_entity.email,
        cellphone=user_entity.cellphone,
        available=user_entity.available
    )


UserEntity.to_domain = to_domain
