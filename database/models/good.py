from sqlalchemy.orm import Mapped
from database.models.base import Base


class Good(Base):
    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[int]
    amount: Mapped[int]
