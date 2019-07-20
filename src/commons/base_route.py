from abc import ABC, abstractmethod

from src.application.boot import Boot


class BaseRoute(ABC):
    @classmethod
    def add_route(cls, uri_templates: str, resource: object, **kwargs):
        Boot().api.add_route(uri_template=uri_templates, resource=resource, **kwargs)
