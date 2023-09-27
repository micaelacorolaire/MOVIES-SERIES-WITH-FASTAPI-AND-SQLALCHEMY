from fastapi import APIRouter,Path,Query
from models import movies

router=APIRouter()

@router.get('/series')
def add_series():
    return ''

@router.delete('/series/{id}')
def delete_series(series:str,id:int):
    return ''

@router.post('/series/{id}')
def post_series(series:str,id:int):
    pass