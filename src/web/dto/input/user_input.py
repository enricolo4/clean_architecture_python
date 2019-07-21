from datetime import datetime
from dataclasses import dataclass
from src.usecases.entity.user import UserEntity


@dataclass
class UserInput:
    name: str
    surname: str
    birthday: datetime
    age: int
    cpf: str
    email: str
    cellphone: str

    @property
    def to_entity(self) -> UserEntity:
        return UserEntity(
            name=self.name,
            surname=self.surname,
            birthday=self.birthday,
            age=self.age,
            cpf=self.cpf,
            email=self.email,
            cellphone=self.cellphone
        )
