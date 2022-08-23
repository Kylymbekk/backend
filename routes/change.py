from fastapi import APIRouter

router = APIRouter()


@router.get('/kgs')
def change_kgs():
    return 'change kgz'


@router.get('/usd')
def change_usd():
    return 'change usd'


@router.get('/rub')
def change_rub():
    return 'change rub'
