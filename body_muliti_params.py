# -*- coding: UTF-8 -*-
"""
@Summary : 
@Author  : marvin
@Time    : 2020/6/13 5:48 下午
@Log     :
           author datetime(DESC) summary
"""
from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    title: str
    desc: str


class User(BaseModel):
    name: str
    age: int


@app.post('/items/')
async def get_all(
        *,
        user: User,
        item: Item,
        q: bool = True,
        importance: int = Body(...)
):
    result = {}
    if user:
        result['user'] = user.dict()
    if item:
        result['item'] = item.dict()
    if q:
        result['q'] = True
    if importance:
        result['importance'] = importance
    return result


@app.post('/single')
async def get_single(
        q: bool,
        user: User,
):
    return {'user': user.dict()}
