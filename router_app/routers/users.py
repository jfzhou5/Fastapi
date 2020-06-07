from fastapi import APIRouter

router = APIRouter()


@router.get('/users/', tags=["users"])
async def read_users():
    return [{'username': 'foo'}, {'username': 'bar'}]


@router.get('/users/me', tags=["users"])
async def read_user_me():
    return {'username': 'marvin_z'}


@router.get('/users/{username}', tags=["users"])
async def read_user(username: str):
    return {"username": username}


