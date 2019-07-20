from src.commons.base_route import BaseRoute
from src.web.controller.user_controller import UserController


class UserRoutes(BaseRoute):
    def __init__(self):
        self.add_route('/user', UserController())
