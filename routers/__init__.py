from routers.users import r as users_router
from routers.goods import r as goods_router
from routers.services import r as services_router
from routers.orders import r as orders_router
from routers.ordered_products import r as ordered_products_router
from routers.shopping_carts import r as shopping_carts_router

__all__ = (
    'users_router',
    'goods_router',
    'services_router',
    'orders_router',
    'ordered_products_router',
    'shopping_carts_router',
)
