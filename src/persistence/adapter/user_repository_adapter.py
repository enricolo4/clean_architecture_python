from src.usecases.entity.user import UserEntity
from src.usecases.repository.user_repository import UserRepository


class UserRepositoryAdapter(UserRepository):
    def __init__(self):
        pass

    def save(self, user_entity: UserEntity) -> UserEntity:
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def find_by_id(self):
        pass

    def get_all(self):
        pass
