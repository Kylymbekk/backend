import datetime
import os

from fastapi import APIRouter, Depends, Form, UploadFile
from sqlalchemy.orm import Session
from starlette.responses import FileResponse
from PIL import Image, ImageFont, ImageDraw

from exceptions.ResponseException import ResponseException
from models import Users
from models.news import News
from utils.dependencies import get_db, get_user, get_image_name

router = APIRouter()


@router.get('/get')
def news(db: Session=Depends(get_db), user:Users=Depends(get_user)):
    if user is not None:
        new = db.query(News).limit(100).all()

        return {
            'data': new
        }
    else:
        raise ResponseException(text='invalid token', status=400)


@router.post('/post')
def add_news(image: UploadFile = Form(), title: str = Form(), date: str = Form(), description: str =Form(), db: Session=Depends(get_db), image_name: str=Depends(get_image_name)):
    if not os.path.exists(f'/Users/abcde/Desktop/Python real project/uploads/' + str(datetime.datetime.now().year)):
        os.mkdir(f'/Users/abcde/Desktop/Python real project/uploads/' + str(datetime.datetime.now().year))
    if not os.path.exists(f'/Users/abcde/Desktop/Python real project/uploads/{str(datetime.datetime.now().year)}/{str(datetime.datetime.now().month)}'):
        os.mkdir(f'/Users/abcde/Desktop/Python real project/uploads/{str(datetime.datetime.now().year)}/' + str(datetime.datetime.now().month))
    if not os.path.exists(f'/Users/abcde/Desktop/Python real project/uploads/{str(datetime.datetime.now().year)}/{str(datetime.datetime.now().month)}/{str(datetime.datetime.now().day)}'):
        os.mkdir(f'/Users/abcde/Desktop/Python real project/uploads/{str(datetime.datetime.now().year)}/{str(datetime.datetime.now().month)}/{str(datetime.datetime.now().day)}')

    im = Image.open(image.file)
    im.thumbnail((400, 400))
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype('/Users/abcde/Desktop/Python real project/ass/Roboto-Italic.ttf', 16)
    draw.text((50, 50), '_zakirov00 Megahit', (255, 0, 0), font=font)
    im.save(f'/Users/abcde/Desktop/Python real project/uploads/{str(datetime.datetime.now().year)}/{str(datetime.datetime.now().month)}/{str(datetime.datetime.now().day)}/{image_name}')
    im.close()

    news = News(title=title, date=datetime.datetime.strptime(date, '%d.%m.%Y'), text=description, img=str(datetime.datetime.now().year) + '/' + str(datetime.datetime.now().month) + '/' + str(datetime.datetime.now().day) + '/' + image_name)
    db.add(news)
    db.commit()

    return 'success'


@router.get('/get_image/{year}/{month}/{day}/{name}')
def get_image(name: str, year: str, month: str, day: str):
    return FileResponse(f'/Users/abcde/Desktop/Python real project/uploads/{year}/{month}/{day}/{name}')


# 2 3 сурот кошуу базага


