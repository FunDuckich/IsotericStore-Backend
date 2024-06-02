from fastapi import APIRouter

r = APIRouter(
    prefix='/goods',
    tags=['Товары'],
)


@r.get('/')
def get_all():
    ...


@r.get('/{good_id}')
def get_by_id(good_id: int):
    ...


@r.post('/')
def add_one():
    ...


@r.delete('/{good_id}')
def remove_one(good_id: int):
    ...


@r.put('/{good_id}')
def update_one(good_id: int):
    ...
