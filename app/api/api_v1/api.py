from fastapi import APIRouter

from .endpoints.hello import router as hello_router
from .endpoints.products import router as products_router

router = APIRouter()
router.include_router(hello_router)
router.include_router(products_router)
