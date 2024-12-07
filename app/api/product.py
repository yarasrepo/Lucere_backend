from fastapi import APIRouter, HTTPException
from app.crud.product import get_all_products, get_product_by_ingredient

router = APIRouter()

@router.get("/products/")
async def get_products():
    products = get_all_products()
    return {"products": products}

@router.get("/products/{product_ingr}")
async def get_product(product_ingr: str):
    product = get_product_by_ingredient(product_ingr)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"product": product}