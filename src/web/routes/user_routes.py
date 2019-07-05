from falcon import API

from src.commons.base_route import BaseRoute
from src.web.controller.user_controller import UserController


class UserRoutes(BaseRoute):

    def routes(self, api: API) -> API:
        api.add_route('/user', UserController())

        return api
