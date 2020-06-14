# -*- coding: UTF-8 -*-
"""
@Summary : 
@Author  : marvin
@Time    : 2020/6/13 2:23 下午
@Log     :
           author datetime(DESC) summary
"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    age: int
    desc: str = '个人描述'


@app.post('/items/', )
async def create_item(item: Item = None):
    return {"data": item.dict()}
