from abc import ABC, abstractmethod

from falcon import API


class BaseRoute(ABC):
    def __init__(self, api: API):
        self.routes(api)

    @abstractmethod
    def routes(self, api: API) -> API:
        pass
