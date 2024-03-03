from fastapi import FastAPI
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from app.db.filedb import products_list, db_remove_product

from .api.api_v1.api import router as api_router
from .core.config import ALLOWED_HOSTS, API_V1_STR, PROJECT_NAME
from .core.errors import http_422_error_handler, http_error_handler
# from .db.mongodb_utils import close_mongo_connection, connect_to_mongo

app = FastAPI(title=PROJECT_NAME)

if not ALLOWED_HOSTS:
    ALLOWED_HOSTS = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def _startup_db_client():
    app.db_remove_product =  db_remove_product
    app.products_list =  products_list

# def _shutdown_db_client():
#     app.mongodb_client.close()

app.add_event_handler("startup", _startup_db_client)
# app.add_event_handler("shutdown", _shutdown_db_client)



app.add_exception_handler(HTTPException, http_error_handler)
app.add_exception_handler(HTTP_422_UNPROCESSABLE_ENTITY, http_422_error_handler)

app.include_router(api_router, prefix=API_V1_STR)
