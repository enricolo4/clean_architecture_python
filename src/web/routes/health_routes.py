from src.web.commons.base_route import BaseRoute
from src.web.controller.health_controller import HealthController


class HealthRoutes(BaseRoute):

    def __init__(self):
        self.add_route('/health', HealthController())
