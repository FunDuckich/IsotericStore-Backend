from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database.models import db_helper
from database.operations.good import (Good,
                                      GoodAdd,
                                      GoodUpdate,
                                      get_all_goods,
                                      get_good,
                                      add_good,
                                      good_by_id,
                                      update_good,
                                      delete_good)

r = APIRouter(
    prefix='/goods',
    tags=['Товары'],
)


@r.get('/', response_model=list[Good])
async def get_all(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await get_all_goods(session=session)


@r.get('/{good_id}/', response_model=Good)
async def get_by_id(good: Good = Depends(good_by_id)):
    return good


@r.post('/', response_model=Good)
async def add_one(good_in: GoodAdd,
                  session: AsyncSession = Depends(db_helper.session_dependency)):
    return await add_good(session=session, good_in=good_in)


@r.put('/{good_id}/', response_model=Good)
async def update_one(good_update: GoodUpdate,
                     good: Good = Depends(good_by_id),
                     session: AsyncSession = Depends(db_helper.session_dependency)):
    return await update_good(session=session,
                             good=good,
                             good_update=good_update)


@r.delete('/{good_id}/', status_code=status.HTTP_204_NO_CONTENT)
async def remove_one(good: Good = Depends(good_by_id),
                     session: AsyncSession = Depends(db_helper.session_dependency)):
    await delete_good(session=session, good=good)
