from contextlib import asynccontextmanager

from fastapi import FastAPI
from routers import (users_router,
                     goods_router,
                     services_router,
                     orders_router,
                     ordered_products_router,
                     shopping_carts_router)
from database.models import Base, db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)

    yield


app = FastAPI(
    title='IsotericStore',
    lifespan=lifespan,
)

app.include_router(users_router)
app.include_router(goods_router)
app.include_router(services_router)
app.include_router(orders_router)
app.include_router(ordered_products_router)
app.include_router(shopping_carts_router)
