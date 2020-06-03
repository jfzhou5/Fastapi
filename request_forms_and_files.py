from fastapi import FastAPI, Form, UploadFile, File

app = FastAPI()


@app.post('/files/')
async def create_file(
        *,
        file: bytes = File(...),
        fileb: UploadFile = File(...),
        token: str = Form(...),  # Form在后

):
    return {
        'token': token,
        'file_size': len(file),
        'fileb_name': fileb.filename
    }
