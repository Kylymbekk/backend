from fastapi import APIRouter

router = APIRouter()


@router.get('/')
def history():
    return 'history'

