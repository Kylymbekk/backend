import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models import Auth, Contacts
from models.users import Users
from utils.dependencies import get_auth, get_user, get_db

router = APIRouter()


@router.get('/get')
def users(user: Users = Depends(get_user), auth: Auth = Depends(get_auth)):
    message = auth.messages
    contacts = auth.contacts
    return {
        'data': user,
        'status': 'success',
        'message': message,
        'contacts': contacts
    }


@router.post('/post')
def add_contact(auth: Auth = Depends(get_auth), db:Session=Depends(get_db)):
    date = '12.05.1999 19:00:30'
    contact = Contacts(
        type='whatsapp',
        value='superman',
        start_at=datetime.datetime.strptime(date,'%d.%m.%Y %H:%M:%S'),
        end_at=datetime.datetime.now(),    )
#    db.add(contact)
    auth.contacts.append(contact)


    return {
        'status': 'success'
    }
