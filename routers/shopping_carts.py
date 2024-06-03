from fastapi import APIRouter

r = APIRouter(
    prefix='/shopping_cart',
    tags=['Корзина'],
)


@r.get('/')
def get_all():
    ...


@r.get('/{cart_item_id}')
def get_by_id(cart_item_id: int):
    ...


@r.post('/')
def add_one():
    ...


@r.delete('/{cart_item_id}')
def remove_one(cart_item_id: int):
    ...
