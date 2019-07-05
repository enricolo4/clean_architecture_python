from falcon import API

from src.commons import BaseRoute
from src.web.controller.health_controller import HealthController


class HealthRoutes(BaseRoute):

    def routes(self, api: API) -> API:
        api.add_route('/health', HealthController())

        return api
