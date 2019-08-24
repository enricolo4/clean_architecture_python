import falcon

from src.application.containers.container import UseCases, Adapters
from src.utils.singleton import Singleton


class Boot(metaclass=Singleton):
    def __init__(self):
        self.__container = self.__init_container
        self.__api: falcon.API = falcon.API()

    @property
    def api(self):
        return self.__api

    @property
    def __init_container(self):
        return UseCases(adapters=Adapters())

    @property
    def service(self):
        return self.__container
