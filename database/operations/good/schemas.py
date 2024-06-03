from pydantic import BaseModel, ConfigDict


class GoodBase(BaseModel):
    name: str
    description: str
    price: int
    amount: int


class GoodAdd(GoodBase):
    ...


class GoodUpdate(GoodAdd):
    ...


class Good(GoodBase):
    model_config = ConfigDict(from_attributes=True)

    id: int