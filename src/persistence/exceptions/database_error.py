from falcon import HTTPInternalServerError


class DataBaseException(HTTPInternalServerError):
    def __init__(self, title: str, description: str):
        super().__init__(title=title, description=description)