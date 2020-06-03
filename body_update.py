from typing import List

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str = None
    description: str = None
    price: float = None
    tax: float = 10.5
    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    return items[item_id]


# update with "PUT"  全替代
@app.put("/items/{item_id}", response_model=Item)
async def update_item_put(item_id: str, item: Item):
    print(item)
    print(type(item))
    update_item_encoded = jsonable_encoder(item)
    items[item_id] = update_item_encoded
    return update_item_encoded


# update with "PATCH" 部分替代
@app.patch("/items/{item_id}", response_model=Item)
async def patch_item(item_id: str, item: Item):
    stored_item_model = Item(**items[item_id])
    update_data = item.dict(exclude_unset=True)
    update_item_model = stored_item_model.copy(update=update_data)
    items[item_id] = jsonable_encoder(update_item_model)
    return update_item_model
