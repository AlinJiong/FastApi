from typing import Union
from fastapi import FastAPI


app = FastAPI()


@app.get('/item/{id}')
async def user_item(id: int, skip: int = 0, limit: Union[int, None] = None):
    item = {'item_id': id, 'skip': skip, 'limit': limit}
    return item
