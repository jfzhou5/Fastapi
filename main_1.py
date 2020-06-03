from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = 10.5
    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2, 'jj': 'dd'},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

# @app.get('/items/{item_id}', response_model=Item, response_model_skip_defaults=True)
"""
response_model_skip_defaults=True 
    会自动忽略未匹配的且拥有默认值的值，仅返回显式设置的值。
    当提供的值和默认值相同时，fastapi仍会显示
response_model_exclude=['name', 'price','ii']
    将会过滤掉model中的相应属性
response_model_include=['tax', 'name']
    将会只保留相应的属性，当include和exclude中有相同的属性时，exclude的优先级高，不取决于顺序
    使用list即可，底层都会set(list())
"""


@app.get('/items/{item_id}', response_model=Item, )
async def get_item_all(item_id: str):
    return items[item_id]


@app.get('/items/{item_id}/public', response_model=Item, response_model_exclude=['price', 'tax'])
async def get_item_data_public(item_id: str):
    return items[item_id]


@app.get('/items/{item_id}/name', response_model=Item, response_model_include=['name'])
async def get_item_data_name(item_id: str):
    return items[item_id]
