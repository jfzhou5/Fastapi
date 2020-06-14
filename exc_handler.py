# -*- coding: UTF-8 -*-
"""
@Summary : 
@Author  : marvin
@Time    : 2020/6/13 8:31 下午
@Log     :
           author datetime(DESC) summary
"""
from fastapi import FastAPI, HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse

app = FastAPI()


class MyException(Exception):
    """
    自定义异常处理类
    """

    def __init__(self, name):
        self.name = name


@app.exception_handler(MyException)
async def my_exc_handler(request: Request, exc: MyException):
    return JSONResponse(
        status_code=400,
        content={'message': f'{exc.name} 您的请求参数有误，请检查后重试'}
    )


@app.get('/')
async def get_all(item: int = 0):
    if item != 3:
        raise HTTPException(status_code=401, detail="401")
    return {'item': item}


@app.get('/exc')
async def test_exc(
        item: int
):
    if item != 3:
        raise MyException(name='marvin')
    return {'item': item}
