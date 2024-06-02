from fastapi import APIRouter

r = APIRouter(
    prefix='/orders',
    tags=['Заказы'],
)


@r.get('/')
def get_all():
    ...


@r.get('/{order_id}')
def get_by_id(order_id: int):
    ...


@r.post('/')
def add_one():
    ...


@r.delete('/{order_id}')
def remove_one(order_id: int):
    ...


@r.put('/{order_id}')
def update_one(order_id: int):
    ...
