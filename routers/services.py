from fastapi import APIRouter

r = APIRouter(
    prefix='/services',
    tags=['Услуги'],
)


@r.get('/')
def get_all():
    ...


@r.get('/{service_id}')
def get_by_id(service_id: int):
    ...


@r.post('/')
def add_one():
    ...


@r.delete('/{service_id}')
def remove_one(service_id: int):
    ...


@r.put('/{service_id}')
def update_one(service_id: int):
    ...
