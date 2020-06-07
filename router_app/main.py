from fastapi import FastAPI, Header, HTTPException, Depends

from router_app.routers import users, items

app = FastAPI()


async def get_token_header(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


app.include_router(users.router)
app.include_router(
    items.router,
    prefix='/items',
    tags=['items'],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

# master
