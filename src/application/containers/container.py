from dependency_injector import containers, providers

from src.usecases.service.user_service import UserService
from src.persistence.repository.user_repository import UserRepository


class Adapters(containers.DeclarativeContainer):
    user_repository_adapter = providers.Singleton(UserRepository)


class UseCases(containers.DeclarativeContainer):
    adapters = providers.DependenciesContainer()

    user_service = providers.Factory(
        UserService,
        user_repository_adapter=adapters.founder_repository_adapter
    )