from falcon import Request, Response, HTTP_OK

import ujson
from falcon.media.validators import jsonschema
from src.web.dto.input.user_input import UserInput
from src.web.dto.input.schemas.user_shcema import user
from src.usecases.service.user_service import UserService


class UserController:
    def __init__(self, user_service: UserService):
        self.__user_service = user_service

    @jsonschema.validate(user)
    def on_post(self, req: Request, resp: Response):
        user_response = self.__user_service.save(UserInput(**req.media).to_entity)

        resp.body = ujson.dumps(user_response.__dict__)
        resp.status = HTTP_OK
