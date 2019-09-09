from dependency_injector import containers, providers

from src.usecases.service.user_service import UserService
from src.persistence.adapter.user_repository_adapter import UserRepositoryAdapter


class Adapters(containers.DeclarativeContainer):
    user_repository_adapter = providers.Singleton(UserRepositoryAdapter)


class UseCases(containers.DeclarativeContainer):
    adapters = providers.DependenciesContainer()

    user_service = providers.Factory(
        UserService,
        user_repository=adapters.user_repository_adapter
    )
