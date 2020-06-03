"""
extra_model 使用多个模型
"""
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
import hashlib

app = FastAPI()

"""
class UserIn(BaseModel):
    '''用户输入的信息模型'''
    name: str
    password: str
    email: EmailStr
    full_name: str


class UserOut(BaseModel):
    '''用以用户查询的信息模型'''
    name: str
    email: EmailStr
    full_name: str


class UserInDB(BaseModel):
    '''用以存储在数据库中的信息模型'''
    name: str
    hash_passwd: str
    email: EmailStr
    full_name: str
"""


class UserBase(BaseModel):
    name: str
    email: EmailStr
    full_name: str


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    pass


class UserInDB(UserBase):
    hash_passwd: str


def get_hash_passwd(password: str):
    """获取密码的hash密文"""
    md5 = hashlib.md5()
    md5.update((password + 'dxchain').encode())
    return md5.hexdigest()


def save_user(user_in: UserIn):
    """保存用户"""
    hash_passwd = get_hash_passwd(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hash_passwd=hash_passwd)
    print(f"user save in db :{user_in_db.dict()}")
    return user_in_db


@app.post('/user/', response_model=UserOut)
async def create_user(*, user_in: UserIn):
    saved_user = save_user(user_in)
    return saved_user
