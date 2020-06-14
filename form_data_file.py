"""
python-multipart
接受的是表单数据而不是json数据
"""

from fastapi import FastAPI, Form, File

app = FastAPI()


@app.post('/login/')
async def login(
        *,
        username: str = Form(...),  # ... 表示占位符
        password: str = Form(...)
):
    return {'username': username}


@app.post('/files/')
async def get_file(file: bytes = File(...)):    # file参数使用bytes类型
    # fastapi 会将file转化为bytes类型   File类型的内容是将内容保存在内存中的，比较适合小型文件。
    return {'file_size': len(file)}



