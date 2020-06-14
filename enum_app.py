# -*- coding: UTF-8 -*-
"""
@Summary : 
@Author  : marvin
@Time    : 2020/6/13 1:50 下午
@Log     :
           author datetime(DESC) summary
"""
from enum import Enum

from fastapi import FastAPI

app = FastAPI()


class Name(str, Enum):
    allan = 'allan'
    bob = 'bob'
    marvin = 'marvin'


@app.get(
    '/{name}/'
)
async def get_name(name: Name):
    if name.value == 'allan':
        return {'name': name.value}
    if name.value == Name.bob:
        return {'name': Name.bob}
    return {'name': 'marvin'}
