from fastapi import APIRouter

r = APIRouter(
    prefix='/ordered_products',
    tags=['Позиции в заказах'],
)


@r.get('/')
def get_all():
    ...


@r.get('/{ordered_product_id}')
def get_by_id(ordered_product_id: int):
    ...


@r.post('/')
def add_new():
    ...


@r.delete('/{ordered_product_id}')
def remove_one(ordered_product_id: int):
    ...


@r.put('/{ordered_product_id}')
def update_one(ordered_product_id: int):
    ...
