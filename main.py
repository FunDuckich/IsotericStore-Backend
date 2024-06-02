from fastapi import FastAPI
from routers import (users_router,
                     goods_router,
                     services_router,
                     orders_router,
                     ordered_products_router, )

app = FastAPI(
    title='IsotericStore',
)

app.include_router(users_router)
app.include_router(goods_router)
app.include_router(services_router)
app.include_router(orders_router)
app.include_router(ordered_products_router)

# имбуля
