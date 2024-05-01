from fastapi import APIRouter

from .endpoints.hello import router as hello_router
from .endpoints.products import router as products_router
from .endpoints.add_to_card import router as add_to_card_router
from .endpoints.do_like import router as do_like_router
from .endpoints.checkout import router as checkout_router
from .endpoints.remove_from_card import router as remove_from_card
from .endpoints.card_products_list import router as card_products_list

router = APIRouter()
router.include_router(hello_router)
router.include_router(products_router)
router.include_router(add_to_card_router)
router.include_router(do_like_router)
router.include_router(checkout_router)
router.include_router(remove_from_card)
router.include_router(card_products_list)
