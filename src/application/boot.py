import falcon


class Singleton(type):
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class Boot(metaclass=Singleton):
    def __init__(self):
        self.__api: falcon.API = falcon.API()
    
    @property
    def api(self):
        return self.__api