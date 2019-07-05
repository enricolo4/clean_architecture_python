from falcon import API

from commons.base_route import BaseRoute
from src.web.controller.health_controller import HealthController


class HealthRoutes(BaseRoute):

    def routes(self, api: API) -> API:
        api.add_route('/health', HealthController())

        return api
