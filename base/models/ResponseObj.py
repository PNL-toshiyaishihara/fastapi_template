from pydantic import BaseModel


class ErrorResponse(BaseModel):
    json_dict: dict
