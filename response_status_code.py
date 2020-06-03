from fastapi import FastAPI
from starlette.status import HTTP_201_CREATED  # 从响应码库中获取响应码常量

app = FastAPI()


# @app.post('/items/', status_code=201)  # 201：created
@app.post('/items/', status_code=HTTP_201_CREATED)  # HTTP_201_CREATED=201
async def create_item(name: str):
    return {'item_name': name}
