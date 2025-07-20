from fastapi import APIRouter, Depends, status, HTTPException
from typing import Annotated
from slugify import slugify
from sqlalchemy.ext.asyncio import AsyncSession
from app.backend.db_depends import get_db
from sqlalchemy import select, insert
from app.schemas import CreateProduct
from app.models import *
from app.routers.auth import get_current_user

router = APIRouter(prefix='/reviews', tags=['reviews'])


@router.get('/')
async def all_reviews(db: Annotated[AsyncSession, Depends(get_db)]):
    review = await db.scalars(select(Review).where(Review.is_active == True))
    all_reviews = review.all()
    if not all_reviews:
        raise HTTPException(status_code=404, detail="No reviews found")
    return all_reviews



# @router.get('/')
# async def all_products(db: Annotated[AsyncSession, Depends(get_db)]):
#     products = await db.scalars(select(Product).where(Product.is_active == True, Product.stock > 0))
#     all_products = products.all()
#     if not all_products:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail='There are no product'
#         )
#     return all_products



@router.get('/{product_name}')
async def products_reviews():
    pass


@router.post('/')
async def add_review():
    pass


@router.delete('/')
async def delete_reviews():
    pass
