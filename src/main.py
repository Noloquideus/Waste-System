from contextlib import asynccontextmanager

from fastapi import FastAPI, APIRouter
from fastapi.openapi.docs import get_swagger_ui_html
from starlette.middleware.cors import CORSMiddleware

from src.presentation.api.organization.router import organization_router
from src.presentation.api.storage.router import storage_router


@asynccontextmanager
async def lifespan(_):
    print('Application is starting...')
    yield
    print('Application is shutting down...')


app = FastAPI(title='Waste System', version='0.0.1', redoc_url=None, docs_url='/api/', lifespan=lifespan)
app_router = APIRouter(prefix='/api')
app_router.include_router(organization_router)
app_router.include_router(storage_router)
app.include_router(app_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/api/docs', include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + ' - Swagger UI',
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url='https://unpkg.com/swagger-ui-dist@5/swagger-ui-bundle.js',
        swagger_css_url='https://unpkg.com/swagger-ui-dist@5/swagger-ui.css')

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='localhost', port=8000)
