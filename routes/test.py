from datetime import date

from fastapi import APIRouter, BackgroundTasks, Depends
from sqlalchemy.orm import Session

from models.news import News
from utils.dependencies import get_db

router = APIRouter()


def task(n: int, db: Session=Depends(get_db)):
    for i in range(n):
        user = News(title='welcome ' + str(i+1), date=date(2022, 8, 10), text='hello ' + str(i+1), img='https://www.megacom.kg/uploads/post/preview/5192/%D0%9F%D0%B0%D1%81%D0%BF%D0%BE%D1%80%D1%82_MP_252-177_%D0%BA%D1%80.jpg')
        db.add(user)
    db.commit()


@router.get('/test')
def test(backgroundTask: BackgroundTasks):
    backgroundTask.add_task(task, 1000)
    return 'ok'
