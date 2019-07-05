from dataclasses import dataclass

from src.usecases.entity.user import UserEntity


@dataclass
class UserInput:
    name: str
    surname: str
    age: int
    cpf: str
    email: str
    cellphone: str

    @property
    def to_entity(self) -> UserEntity:
        return UserEntity(
            name=self.name,
            surname=self.surname,
            age=self.age,
            cpf=self.cpf,
            email=self.email,
            cellphone=self.cellphone
        )
