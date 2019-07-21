import json
from falcon import HTTP_OK


class HealthController:

    @staticmethod
    def on_get(req, res):
        res.body = json.dumps({'status': 'ok'})
        res.status = HTTP_OK
