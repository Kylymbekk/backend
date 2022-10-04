from fastapi import UploadFile
from pydantic import BaseModel


class NewsPost(BaseModel):
    title: str
    date: str
    description: str
    image: UploadFile

