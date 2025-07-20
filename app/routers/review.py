from datetime import datetime

from fastapi import APIRouter, Depends, status, HTTPException
from typing import Annotated
from slugify import slugify
from sqlalchemy.ext.asyncio import AsyncSession
from app.backend.db_depends import get_db
from sqlalchemy import select, insert
from app.schemas import CreateReview
from app.models import *
from app.routers.auth import get_current_user

router = APIRouter(prefix='/reviews', tags=['reviews'])


@router.get('/')
async def all_reviews(db: Annotated[AsyncSession, Depends(get_db)]):
    review = await db.scalars(select(Review).where(Review.is_active == True))
    all_reviews = review.all()
    if not all_reviews:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No reviews found")
    return all_reviews


@router.get('/{product_name}')
async def products_reviews():
    pass


@router.post('/')
async def add_review(db: Annotated[AsyncSession, Depends(get_db)], product_id: int, create_review: CreateReview,
                     get_user: Annotated[dict, Depends(get_current_user)]):
    if get_user.get('is_supplier') or get_user.get('is_admin'):
        product = await db.scalars(select(Product).where(Product.id == create_review.product_id))
        if not product is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No product found")
        await db.execute(insert(Review).values(product_id=create_review.product_id,
                                               user_id=get_user.get('id'),
                                               comment=create_review.comment,
                                               comment_data=datetime.now()
                                               ))
        await db.commit()
        return {
            'status_code': status.HTTP_201_CREATED,
            'message': 'Review added',
            'user_id': get_user.get('id'),
        }


@router.delete('/')
async def delete_reviews():
    pass
