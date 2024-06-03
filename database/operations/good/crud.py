from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from sqlalchemy import select
from database.models import Good
from typing import Union
from database.operations.good.schemas import GoodAdd, GoodUpdate


async def get_all_goods(session: AsyncSession) -> list[Good]:
    stmt = select(Good).order_by(Good.id)
    result: Result = await session.execute(stmt)
    goods = result.scalars().all()
    return list(goods)


async def get_good(session: AsyncSession, good_id: int) -> Union[Good, None]:
    good = await session.get(Good, good_id)
    return good


async def add_good(session: AsyncSession, good_in: GoodAdd) -> Good:
    new_good = Good(**good_in.model_dump())
    session.add(new_good)
    await session.commit()
    await session.refresh(new_good)
    return new_good


async def update_good(session: AsyncSession,
                      good_update: GoodUpdate,
                      good: Good) -> Good:
    for name, value in good_update.model_dump().items():
        setattr(good, name, value)
    await session.commit()
    return good


async def delete_good(session: AsyncSession,
                      good: Good) -> None:
    await session.delete(good)
    await session.commit()
