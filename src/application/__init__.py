from src.application.boot import Boot
from src.web.routes.user_routes import UserRoutes
from src.web.routes.health_routes import HealthRoutes

api = Boot().api

HealthRoutes()
UserRoutes()