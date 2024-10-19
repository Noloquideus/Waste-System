from fastapi import APIRouter

storage_router = APIRouter(prefix='/storage', tags=['Storage'])

@storage_router.post(path='/', status_code=201)
async def create_storage():
    pass

@storage_router.get(path='/', status_code=200)
async def get_storages():
    pass

@storage_router.get(path='/{storage_id}', status_code=200)
async def get_storage(storage_id):
    pass

@storage_router.put(path='/{storage_id}', status_code=200)
async def update_storage(storage_id):
    pass

@storage_router.delete(path='/{storage_id}', status_code=200)
async def delete_storage(storage_id):
    pass