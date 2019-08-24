from src.usecases.entity.user import UserEntity
from src.usecases.repository.user_repository import UserRepository

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.__user_repository = user_repository

    def save(self, user_entity: UserEntity) -> UserEntity:
        return self.__user_repository.save(user_entity)

    def update(self):
        return self.__user_repository.update()

    def delete(self):
        return self.__user_repository.delete()

    def find_by_id(self):
        return self.__user_repository.find_by_id()

    def get_all(self):
        return self.__user_repository.get_all()
