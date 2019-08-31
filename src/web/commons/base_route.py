from abc import ABC

from src.application.boot import Boot
from src.application.containers.container import UseCases, Adapters


class BaseRoute(ABC):

    @classmethod
    def add_route(cls, uri_templates: str, resource: object, **kwargs):
        Boot().api.add_route(uri_template=uri_templates, resource=resource, **kwargs)

    @property
    def services(self) -> UseCases:
        return Boot().service
