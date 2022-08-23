from pydantic import BaseModel


class TransferPost(BaseModel):
    token: str
    balance: int
    email: str