import falcon

from src.utils.singleton import Singleton


class Boot(metaclass=Singleton):
    def __init__(self):
        self.__api: falcon.API = falcon.API()
    
    @property
    def api(self):
        return self.__api