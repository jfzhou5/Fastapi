from enum import Enum
from typing import List

from fastapi import FastAPI, Query, Path
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


@app.get("/")
def read_root():
    return {'key': 'value'}  # 返回json字符串


@app.get('/items/{item_id}')
def read_item(item_id: int, q: str = 'a'):
    return {'item_id': item_id, 'q': q + str(item_id), 'list': [1, 3, 4]}


@app.get('/items/2')  # 和上一个视图函数冲突了，两者应用哪一个取决于顺序
def read_item_id():
    return {"item": 2}


@app.put('/items/{item_id}')
def put_item(item_id: int, item: Item):
    return {'item_name': item.name, "item_id": item_id}


# 获取路径中的path参数 Path Parammeters
@app.get('/path/{item_path:path}')  # path：参数应该匹路径型的
def get_path(item_path: str):
    return {'item_path': item_path}


# 预定义路径参数值 predefined values
class ModeLName(str, Enum):  # 继承自Enum类
    a = 'a'
    b = 'b'
    c = 'c'


@app.get('/predefined/{model_name}')
def predefined(model_name: ModeLName):
    if model_name == ModeLName.a:
        return {'model_name': ModeLName.a}
    if model_name.value == 'c':
        return {'model_name': model_name.value}
    return {'model_name': ModeLName.b}


# Query Parammeters 查询参数
# a，b 参数均为非路径参数，即为查询参数用？，&标识；
# a 未设置默认值 表示必须有的查询参数
# b 设置默认值为 0，非必须有查询参数，默认值为0
# c 可选查询参数 ，默认为None
@app.get('/query_param')
def query_param(a: int, b: int = 0, c: int = None):
    return {'a': a, 'b': b, 'c': c}


# Query parameter type conversion 查询参数的类型转换
@app.get('/conver_type/{value:int}')
def conver_type(value, bool_param: bool = False):
    return {'value': value, 'bool_param': bool_param}


# 请求正文 request body
class Items(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


@app.post('/request_body')
async def create_item(item: Items):
    print(item.dict())
    return item


# 查询参数和字符串验证 Query Parameters and String Validations
@app.get('/query_validate')
async def query_validate(
        q: str = Query(
            None,
            max_length=3,
            min_length=1,
            title='qdd',
            description='q value',  # 描述
            deprecated=True,  # 表示是否为弃用参数
            alias='q的别名'
        )
):
    # 可选参数 不提供时，默认值为None；提供时，最小/大长度有限制
    # 默认值设置为 ... 占位符时，代表该参数是必须的
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({'q': q})
    return results


# 获取多个参数列表值
@app.get('/querys')
async def get_querys(q: List[str] = Query(None)):
    # Query(['foo','bar']) 具备多个默认值的列表
    return {'Q': q}


# Path Parameters and Numeric Validations 路径参数和数值验证
@app.get("/itemss/{item_id}")
async def read_items(
        *,
        item_id: int = Path(..., title="The ID of the item to get"),
        q: str = None,
        a=1
):
    results = {"item_id": item_id}
    print(a)
    if q:
        results.update({"q": q})
    return results


