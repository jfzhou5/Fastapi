# -*- coding: UTF-8 -*-
"""
@Summary : 
@Author  : marvin
@Time    : 2020/6/13 2:03 下午
@Log     :
           author datetime(DESC) summary
"""
from fastapi import FastAPI

app = FastAPI()

items = [
    {'num': 1},
    {'num': 2},
    {'num': 3},
    {'num': 4},
    {'num': 5}
]


@app.get('/')
async def all_items():
    return items


@app.get('/items/')
async def read_items(start: int, end: int = 10):
    return items[start:end]
