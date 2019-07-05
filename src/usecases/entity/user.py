from dataclasses import dataclass


@dataclass
class UserEntity:
    name: str
    surname: str
    age: int
    cpf: str
    email: str
    cellphone: str