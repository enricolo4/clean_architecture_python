from abc import ABC, abstractmethod

from src.usecases.entity.user import UserEntity


class UserRepository(ABC):
    @abstractmethod
    def save(self, user_entity: UserEntity) -> UserEntity:
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def find_by_id(self):
        pass

    @abstractmethod
    def get_all(self):
        pass
