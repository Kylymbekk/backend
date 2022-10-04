from pydantic import BaseModel


class TransferPost(BaseModel):
    balance: int
    email: str