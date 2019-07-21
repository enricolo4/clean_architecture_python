from src.usecases.adapter.repository.user_repository_adapter import UserRepositoryAdapter
from src.usecases.entity.user import UserEntity


class UserRepository(UserRepositoryAdapter):
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