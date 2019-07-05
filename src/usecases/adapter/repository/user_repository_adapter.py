from abc import ABC, abstractmethod


class UserRepositoryAdapter(ABC):
    @abstractmethod
    def save(self):
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

