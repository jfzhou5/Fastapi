# -*- coding: UTF-8 -*-
"""
@Summary : 
@Author  : marvin
@Time    : 2020/6/13 12:31 下午
@Log     :
           author datetime(DESC) summary
"""
import uvicorn
from fastapi import FastAPI
from starlette.requests import Request
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get('/')
async def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request, 'hello': 'nihao'})


@app.get('/{item_id}/')
async def get_item(item_id: int, request: Request):
    return templates.TemplateResponse('index.html', {
        'request': request,
        'hello': 'hello',
        'item_id': item_id
    })


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8001)
