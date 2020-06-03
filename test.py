from datetime import datetime
from typing import List
from pydantic import BaseModel


# 类型检测
def add(a: str, b: int):
    return a + str(b)


print(add('1', 1))


# Pydantic 模型
class User(BaseModel):
    id: int
    name: str = 'marvin'
    signup_ts: datetime = None
    friends: List[int] = []


user = User(id=1, signup_ts="2017-06-01 12:22", friends=['1', 2, '2'])
print(user)
print(user.id)
user = User(id='2', signup_ts="2017-06-01 12:22", friends=['1', 2, '2'])
print(user)
print(user.id)
