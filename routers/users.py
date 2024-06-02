from fastapi import APIRouter

r = APIRouter(
    prefix='/users',
    tags=['Пользователи'],
)


@r.get('/')
def get_all():
    ...


@r.get('/{user_id}')
def get_by_id(user_id: int):
    ...


@r.post('/')
def add_one():
    ...


@r.delete('/{user_id}')
def remove_one(user_id: int):
    ...


@r.put('/{user_id}')
def update_one(user_id: int):
    ...
