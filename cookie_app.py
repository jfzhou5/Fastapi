# -*- coding: UTF-8 -*-
"""
@Summary : 
@Author  : marvin
@Time    : 2020/6/13 6:22 下午
@Log     :
           author datetime(DESC) summary
"""
from typing import List

from fastapi import FastAPI, Cookie, Body

app = FastAPI()


@app.post('/cookie/')
async def get_cookie(
        name: List[str] = Body(...)
):
    return {'name': name}
