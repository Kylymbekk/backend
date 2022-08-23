from pydantic import BaseModel
from typing import Union


class NewsPost(BaseModel):
    token: Union[str, None]