import json
from falcon import HTTP_OK

from src.web.routes import api


class HealthController:

    @staticmethod
    @api.add_route()
    def on_get(req, res):
        res.body = json.dumps({'status': 'ok'})
        res.status = HTTP_OK
