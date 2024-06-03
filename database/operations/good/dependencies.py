from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import db_helper, Good
from database.operations.good import get_good


async def good_by_id(good_id: Annotated[int, Path],
                     session: AsyncSession = Depends(db_helper.session_dependency)
                     ) -> Good:
    good = await get_good(session=session, good_id=good_id)
    if good:
        return good
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Товар с айди {good_id} не найден!'
        )
