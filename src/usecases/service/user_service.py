from src.usecases.adapter.repository.user_repository_adapter import UserRepositoryAdapter


class UseService:
    def __init__(self, user_repository_adapter: UserRepositoryAdapter):
        self.__user_repository_adapter = user_repository_adapter

    def save(self):
        return self.__user_repository_adapter.save()

    def update(self):
        return self.__user_repository_adapter.update()

    def delete(self):
        return self.__user_repository_adapter.delete()

    def find_by_id(self):
        return self.__user_repository_adapter.find_by_id()

    def get_all(self):
        return self.__user_repository_adapter.get_all()

